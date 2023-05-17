class Pessoa:  # Super classe
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando......')


class Cliente(Pessoa):  # Sub classe
    def comprar(self):
        print(f'{self.nomeclasse} comprando......')


class Aluno(Pessoa):  # Sub classe
    def estudar(self):
        print(f'{self.nomeclasse} estudando......')
