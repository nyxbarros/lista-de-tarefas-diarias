import subprocess
from pathlib import Path
from app.Conexao import Conexao
import os
import re

class Service:
    @staticmethod
    def entrada_dados():
        arquivo = Path(__file__).resolve().parent.parent / "dados.md"

        # se não existir, cria com conteúdo inicial
        try:
            with open(arquivo, "w", encoding="utf-8") as f:
                f.write(Conexao.string())
        except FileExistsError:
            pass

        # abre o editor do GNOME
        subprocess.run(["gnome-text-editor", arquivo])  # ou "gedit"

        # lê depois de fechar
        with open(arquivo, "r", encoding="utf-8") as f:
            texto = f.read()

        Service.md_para_json(texto)
        os.remove(arquivo)

    @staticmethod
    def md_para_json(md):
        dados = {}
        chave_atual = None

        for linha in md.splitlines():
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

                dados[chave_atual]["tarefas"].append({
                    "feito": feito,
                    "nome": nome,
                    "data": data
                })
        Conexao.salvar(dados)
        Conexao.ordenar()