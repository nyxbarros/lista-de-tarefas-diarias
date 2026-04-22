class Menu:
    def __init__(self, opcoes):
        self.opcoes = opcoes
        self.opcao = None
    
    @staticmethod
    def cabecalho(texto):
        print('='*(len(texto)+4))
        print(f"| {texto} |")
        print('='*(len(texto)+4))
        print()
    
    def menu(self):
        Menu.cabecalho('Gerenciador de Tarefas Diárias')
        
        if (self.opcao is not None) and (self.opcao < len(self.opcoes)):
            print(f'{self.opcoes[self.opcao][0]}:')
            self.opcoes[self.opcao][1]()
            print()

        for i, v in enumerate(self.opcoes):
            print(f'[ {i} ] {v[0]}')
        self.opcao = int(input('Insira a opção desejada: '))