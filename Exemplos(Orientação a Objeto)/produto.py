"""Orientando a Objetos property - Getters e Setters"""


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter
    @property
    def nome(self):
        return self._nome

    # Setter
    @nome.setter
    def nome(self, valor):
        self._nome = valor.replace('a', '@')
        # Essa função title() coloca a primeira letra do texto maiusculo
        # Essa função lower() coloca o texto minusculo
        # Essa função replace() troca as palavras ou letras que contém no texto para o que você deseja alterar

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            # print(valor)
            valor = float(valor.replace('R$', ''))
        self._preco = valor
