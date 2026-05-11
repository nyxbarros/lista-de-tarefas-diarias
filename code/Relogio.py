from builtins import filter
from datetime import datetime, date, timedelta

from textual import filter

from Conexao import Conexao

from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta


class Relogio:
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
                v["tarefas"] = [
                    tarefa
                    for tarefa in v["tarefas"]
                    if not tarefa["feito"]
                ]

        Conexao.salvar(dados)