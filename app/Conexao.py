from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from pathlib import Path
import re
from app.BancoDeDadosJson import BancoDeDadosJson


class Conexao(BancoDeDadosJson):
    arquivo = Path(__file__).resolve().parent.parent / "dados.json"
    BancoDeDadosJson.modelo_inicial = {
        'a cada 1 dia': {
            'limite': (date.today() + timedelta(days=1)).isoformat(),
            'tarefas': []
        },
        'a cada 1 semana': {
            'limite': (date.today() + timedelta(weeks=1)).isoformat(),
            'tarefas': []
        },
        'a cada 1 mes': {
            'limite': (date.today() + relativedelta(months=1)).isoformat(),
            'tarefas': []
        },
        'a cada 1 ano': {
            'limite': (date.today() + relativedelta(years=1)).isoformat(),
            'tarefas': []
        },
        'sem prazo': {
            'tarefas': []
        },
    }

    @staticmethod
    def string():
        dados = BancoDeDadosJson.ler()
        saida = ''

        for k, v in dados.items():
            if 'a cada ' in k:
                saida += f'{k} ({v["limite"]}):\n'
                for tarefa in v['tarefas']:
                    saida += f'- [{"X" if tarefa["feito"] else " "}] {tarefa["nome"]}\n'
                saida += '\n'

        for k, v in dados.items():
            if not 'a cada ' in k:
                saida += f'{k}:\n'
                for tarefa in v['tarefas']:
                    data = tarefa['data']
                    saida += f'- [{"X" if tarefa["feito"] else " "}]{"" if data is None else f" ({data})"} {tarefa["nome"]}\n'
                saida += '\n'

        return saida

    @staticmethod
    def ordenar():
        def prioridade(chave):
            if re.fullmatch(r"a cada \d+ dia", chave):
                return 0
            if re.fullmatch(r"a cada \d+ semana", chave):
                return 1
            if re.fullmatch(r"a cada \d+ mes", chave):
                return 2
            if re.fullmatch(r"a cada \d+ ano", chave):
                return 3
            if re.fullmatch(r"outros", chave):
                return 1000
            return 999

        dados = BancoDeDadosJson.ler()

        dados_ordenados = dict(
            sorted(dados.items(), key=lambda item: prioridade(item[0]))
        )

        for k, v in dados_ordenados.items():
            tarefas = v.get('tarefas', [])

            if tarefas:
                tarefas.sort(key=lambda item: (
                    item['feito'],
                    item.get('data') is None,
                    item.get('data') or ""
                ))

                dados_ordenados[k]['tarefas'] = tarefas

        BancoDeDadosJson.salvar(dados_ordenados)

        return dados_ordenados