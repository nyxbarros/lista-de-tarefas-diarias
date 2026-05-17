import json

from pathlib import Path

class BancoDeDadosJson:
    arquivo = Path(__file__).resolve().parent.parent / "dados.json"
    modelo_inicial = {}

    @staticmethod
    def existe():
        return BancoDeDadosJson.arquivo.is_file()

    @staticmethod
    def salvar(dados):
        with open('dados.json', 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    @staticmethod
    def criar():
        BancoDeDadosJson.salvar(BancoDeDadosJson.modelo_inicial)

    @staticmethod
    def ler():
        if not BancoDeDadosJson.existe():
            BancoDeDadosJson.criar()

        with open(BancoDeDadosJson.arquivo, "r", encoding="utf-8") as f:
           return json.load(f)

    @staticmethod
    def acrescentar(valor, caminho : list, dados):
        if dados == None:
            dados = BancoDeDadosJson.ler()
        chave = caminho[0]

        if len(caminho) == 1:
            if isinstance(dados, dict):
                dados = valor | dados
            else:
                if isinstance(dados, list):
                    if isinstance(valor, list):
                        dados = dados + valor
                    else:
                        dados = dados + [valor]
                else:
                    if isinstance(valor, list):
                        dados = [dados] + valor
                    else:
                        dados = dados + valor

            BancoDeDadosJson.salvar(dados)
            return dados

        if isinstance(dados, dict):
            prox = dados.get(chave)
        else:
            prox = dados[int(chave)]

        BancoDeDadosJson.atualizar(valor, caminho[1:], prox)

        BancoDeDadosJson.salvar(dados)
        return dados

    @staticmethod
    def atualizar(valor, caminho : list, dados):
        if dados == None:
            dados = BancoDeDadosJson.ler()

        chave = caminho[0]

        if len(caminho) == 1:
            if isinstance(dados, dict):
                dados[chave] = valor
            else:
                dados[int(chave)] = valor

            BancoDeDadosJson.salvar(dados)
            return dados

        if isinstance(dados, dict):
            prox = dados.get(chave)
        else:
            prox = dados[int(chave)]

        BancoDeDadosJson.atualizar(valor, caminho[1:], prox)

        BancoDeDadosJson.salvar(dados)
        return dados

    @staticmethod
    def deletar(caminho : list, dados):
        if dados == None:
            dados = BancoDeDadosJson.ler()

        chave = caminho[0]

        if len(caminho) == 1:
            if isinstance(dados, dict):
                dados.pop(chave, None)
            else:
                dados.pop(int(chave))

            BancoDeDadosJson.salvar(dados)
            return dados

        if isinstance(dados, dict):
            prox = dados.get(chave)
        else:
            prox = dados[int(chave)]

        BancoDeDadosJson.deletar(caminho[1:], prox)

        BancoDeDadosJson.salvar(dados)
        return dados