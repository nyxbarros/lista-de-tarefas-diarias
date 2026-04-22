from menu import Menu
from relogio import Relogio
from rotina import Rotina
from datetime import datetime

import json
import os

print(os.path.exists('nome.ext'))

def main():
    if not os.path.isfile('tarefas.json'):
        with open('tarefas.json', 'w') as f:
            dados = {
                "dia": f"{datetime.today().strftime('%Y-%m-%d')}",
                "tarefas": []
            }
            json.dump(dados, f, indent=4)
    opcoes = [
        ['adicionar', Rotina.adicionar] ,
        ['listar', Rotina.mostrar],
        ['(des)fazer', Rotina.fazer],
        ['deletar', Rotina.deletar],
        ['editar', Rotina.editar],
        ['reorganizar', Rotina.reorganizar],
        ['sair', exit]
    ]
    menu_principal = Menu(opcoes)
    while True:
        Relogio.resetar()
        menu_principal.menu()
        os.system('clear')


if __name__ == '__main__':
    main()