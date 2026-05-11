from app.Service import Service
from app.Relogio import Relogio

class Controller:
    @staticmethod
    def main():
        Relogio.resetar()
        print("Lista de tarefas")
        print()
        print('[ 1 ] ver tarefas')
        print('[ 2 ] resetar agenda')
        print('[ 3 ] sair')
        opcao = input('insira a opcao: ').strip()

        if opcao == '1':
            Controller.crud_tarefas()
        elif opcao == '2':
            Controller.resetar_listas()
        elif opcao == '3':
            Controller.sair()
        else:
            print("valor invalido")

    @staticmethod
    def crud_tarefas():
        Service.entrada_dados()

    @staticmethod
    def resetar_listas():
        pass

    @staticmethod
    def sair():
        exit()
