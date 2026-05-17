import subprocess
from pathlib import Path
import os
import re
from builtins import filter

from app.Conexao import Conexao
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

class Service:
    @staticmethod
    def entrada_dados():
        arquivo = Path(__file__).resolve().parent.parent / "dados.md"

        if arquivo.is_file():
            Service.md_para_json(arquivo)

        with open(arquivo, "w", encoding="utf-8") as f:
            f.write(Conexao.string())

        subprocess.run(["gnome-text-editor", arquivo])  # ou "gedit"

        Service.md_para_json(arquivo)

        os.remove(arquivo)


    @staticmethod
    def md_para_json(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            texto = f.read()

        dados = {}
        chave_atual = None

        for linha in texto.splitlines():
            linha = linha.strip()

            if not linha:
                continue

            # 1. cabeçalho com data
            m = re.match(r"(.+)\((\d{4}-\d{2}-\d{2})\):", linha)
            if m:
                chave_atual = m.group(1).strip()
                dados[chave_atual] = {
                    "limite": m.group(2),
                    "tarefas": []
                }
                continue

            # 2. cabeçalho sem data
            m = re.match(r"(.+):$", linha)
            if m and not re.match(r".+\(\d{4}-\d{2}-\d{2}\):", linha):
                chave_atual = m.group(1).strip()
                dados[chave_atual] = {
                    "limite": None,
                    "tarefas": []
                }
                continue

            # 3. tarefas com possível data interna
            m = re.match(r"- \[([ xX])\]\s*(?:\((\d{4}-\d{2}-\d{2})\)\s*)?(.*)", linha)
            if m and chave_atual:
                feito = m.group(1).lower() == "x"
                data = m.group(2)  # pode ser None
                nome = m.group(3).strip()

                if not nome:
                    continue

                if not feito or 'a cada ' in chave_atual:
                    dados[chave_atual]["tarefas"].append({
                        "feito": feito,
                        "nome": nome,
                        "data": data
                    })
        Conexao.salvar(dados)
        Conexao.ordenar()

    @staticmethod
    def resetar():
        dados = Conexao.ler()
        hoje = date.today()

        for k, v in dados.items():

            # listas recorrentes
            if k.startswith('a cada '):

                data_obj = datetime.strptime(
                    v["limite"],
                    "%Y-%m-%d"
                ).date()

                numero, unidade = k.split(' ')[2:4]
                numero = int(numero)

                # reseta tarefas
                if hoje > data_obj:
                    for tarefa in v["tarefas"]:
                        tarefa["feito"] = False

                # avança datas vencidas
                while hoje > data_obj:

                    if unidade == 'dia':
                        data_obj += timedelta(days=numero)

                    elif unidade == 'semana':
                        data_obj += timedelta(weeks=numero)

                    elif unidade == 'mes':
                        data_obj += relativedelta(months=numero)

                    elif unidade == 'ano':
                        data_obj += relativedelta(years=numero)

                # salva nova data
                v["limite"] = data_obj.isoformat()

            # listas normais
            else:
                v["tarefas"] = list(filter(lambda x: not x['feito'], v["tarefas"]))

        Conexao.salvar(dados)
