from datetime import datetime

import json


class Relogio:
    @staticmethod
    def pull_dados():
        with open('tarefas.json', 'r') as f:
            dados = json.load(f)
        return dados
    
    @staticmethod
    def push_dados(dados):
        with open('tarefas.json', 'w') as f:
            json.dump(dados, f, indent=4)
    
    @staticmethod
    def resetar():
        hoje = datetime.today().strftime("%Y-%m-%d")
        dados = Relogio.pull_dados()
        if hoje != dados['dia']:
            dados['dia'] = hoje
            for i in dados['tarefas']:
                i['status'] = False
        Relogio.push_dados(dados)