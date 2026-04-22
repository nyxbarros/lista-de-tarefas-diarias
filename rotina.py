import json

class Rotina:
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
    def adicionar():
        dados = Rotina.pull_dados()
        
        while True:
            tarefa = input('insira o nome da tarefa: ')
            if tarefa != '':
                dados['tarefas'].append({'status': False, 'nome': tarefa})
            else:
                break
        
        Rotina.push_dados(dados)

    @staticmethod
    def mostrar():
        dados = Rotina.pull_dados()
        dados['tarefas'] = sorted(dados['tarefas'], key=lambda x: x['status'])
        for i in sorted(dados['tarefas'], key=lambda x: x['status']):
            print(f'[{"X" if i["status"] else " "}] {i["nome"]}')
        Rotina.push_dados(dados)

    @staticmethod
    def fazer():
        dados = Rotina.pull_dados()
        dados['tarefas'] = sorted(dados['tarefas'], key=lambda x: x['status'])
        formatacao = len(str(len(dados['tarefas'])))
        for i, v in enumerate(sorted(dados['tarefas'], key=lambda x: x['status'])):
            print(f'{i:>{formatacao}} - [{"X" if v["status"] else " "}] {v["nome"]}')
        try:
            opcao = input('Insira quais tarefas devem ser feitas antes (separadas por espaço): ')
            opcao = [int(i) for i in set(opcao.replace(' ','').split(',') if ',' in opcao else opcao.split(' '))]
            for i in opcao:
                dados['tarefas'][i]['status'] = not dados['tarefas'][i]['status']
            Rotina.push_dados(dados)
        except:
            return None

    @staticmethod
    def deletar():
        dados = Rotina.pull_dados()
        dados['tarefas'] = sorted(dados['tarefas'], key=lambda x: x['status'])
        formatacao = len(str(len(dados['tarefas'])))
        for i, v in enumerate(sorted(dados['tarefas'], key=lambda x: x['status'])):
            print(f'{i:>{formatacao}} - [{"X" if v["status"] else " "}] {v["nome"]}')
        try:
            opcao = input('Insira quais tarefas devem ser feitas antes (separadas por espaço): ')
            opcao = [int(i) for i in set(opcao.replace(' ','').split(',') if ',' in opcao else opcao.split(' '))]
            for i in sorted(opcao, reverse=True):
                dados['tarefas'].pop(i)
            Rotina.push_dados(dados)
        except:
            return None

    @staticmethod
    def editar():
        dados = Rotina.pull_dados()
        dados['tarefas'] = sorted(dados['tarefas'], key=lambda x: x['status'])
        formatacao = len(str(len(dados['tarefas'])))
        for i, v in enumerate(sorted(dados['tarefas'], key=lambda x: x['status'])):
            print(f'{i:>{formatacao}} - [{"X" if v["status"] else " "}] {v["nome"]}')
        try:
            opcao = int(input('Insira  qual tarefa (des)fazer: '))
            aux = input('Insira o novo nome: ')
            dados['tarefas'][opcao]['nome'] = aux if aux != '' else dados['tarefas'][opcao]['nome']
            Rotina.push_dados(dados)
        except:
            return None
    
    @staticmethod
    def reorganizar():
        dados = Rotina.pull_dados()
        dados['tarefas'] = sorted(dados['tarefas'], key=lambda x: x['status'])
        formatacao = len(str(len(dados['tarefas'])))
        for i, v in enumerate(sorted(dados['tarefas'], key=lambda x: x['status'])):
            print(f'{i:>{formatacao}} - [{"X" if v["status"] else " "}] {v["nome"]}')
        try:
            opcao = input('Insira quais tarefas devem ser feitas antes (separadas por espaço): ')
            opcao = [int(i) for i in set(opcao.replace(' ','').split(',') if ',' in opcao else opcao.split(' '))]
            lista_atualizada = []

            for i in opcao:
                lista_atualizada.append(dados['tarefas'][i])

            for i in sorted(opcao,reverse=True):
                dados['tarefas'].pop(i)

            dados['tarefas'] = lista_atualizada + dados['tarefas']

            Rotina.push_dados(dados)
        except:
            return None