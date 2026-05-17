from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from pathlib import Path
import re
from app.BancoDeDadosJson import BancoDeDadosJson


class Conexao(BancoDeDadosJson):
    arquivo = Path(__file__).resolve().parent.parent / "dados.json"
    hoje = date.today()
    BancoDeDadosJson.modelo_inicial = {
        'a cada 1 dia': {
            'limite': (hoje + timedelta(days=1)).isoformat(),
            'tarefas': []
        },
        'a cada 1 semana': {
            'limite': (hoje + timedelta(weeks=1)).isoformat(),
            'tarefas': []
        },
        'a cada 1 mes': {
            'limite': (hoje + relativedelta(months=1)).isoformat(),
            'tarefas': []
        },
        'a cada 1 ano': {
            'limite': (hoje + relativedelta(years=1)).isoformat(),
            'tarefas': []
        },
        'domingo': {
            'limite': (hoje + timedelta(days=(7 if hoje.weekday() == 6 else (6 - hoje.weekday()) % 7))).isoformat(),
            'tarefas': []
        },
        'segunda-feira': {
            'limite': (hoje + timedelta(days=(7 if hoje.weekday() == 0 else (0 - hoje.weekday()) % 7))).isoformat(),
            'tarefas': []
        },
        'terça-feira': {
            'limite': (hoje + timedelta(days=(7 if hoje.weekday() == 1 else (1 - hoje.weekday()) % 7))).isoformat(),
            'tarefas': []
        },
        'quarta-feira': {
            'limite': (hoje + timedelta(days=(7 if hoje.weekday() == 2 else (2 - hoje.weekday()) % 7))).isoformat(),
            'tarefas': []
        },
        'quinta-feira': {
            'limite': (hoje + timedelta(days=(7 if hoje.weekday() == 3 else (3 - hoje.weekday()) % 7))).isoformat(),
            'tarefas': []
        },
        'sexta-feira': {
            'limite': (hoje + timedelta(days=(7 if hoje.weekday() == 4 else (4 - hoje.weekday()) % 7))).isoformat(),
            'tarefas': []
        },
        'sábado': {
            'limite': (hoje + timedelta(days=(7 if hoje.weekday() == 5 else (5 - hoje.weekday()) % 7))).isoformat(),
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
            if 'a cada ' in k or k in ['domingo', 'segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado']:
                saida += f'{k} ({v["limite"]}):\n'
                for tarefa in v['tarefas']:
                    saida += f'- [{"X" if tarefa["feito"] else " "}] {tarefa["nome"]}\n'
                saida += '\n'

        for k, v in dados.items():
            if not 'a cada ' in k and not k in ['domingo', 'segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado']:
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
            if 'domingo' == chave:
                return 4
            if 'segunda-feira' == chave:
                return 5
            if 'terça-feira' == chave:
                return 6
            if 'quarta-feira' == chave:
                return 7
            if 'quinta-feira' == chave:
                return 8
            if 'sexta-feira' == chave:
                return 9
            if 'sábado' == chave:
                return 10
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