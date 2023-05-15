from random import randint


class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # Usando o decorator @classmethod não usamos a instância self que fica na function def __init__
    # A partir desse momento criamos uma função que será usado dentro da class Pessoa, e instânciamos usando cls como no exemplo abaixo
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    # Usando o decorator @staticmethod e como tivessemos criando uma função normal fora da classe, ele não tem acesso nenhum as instância da class
    # é do classmethod mais essa função pode ser chamado quando usamos tanto a class como neste exemplo
    # Pessoa.gera_id() ou também usando a classe construtora como p1.gera_id()
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand
