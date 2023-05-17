from classes import *

"""
TODOS OS TIPOS DE CLASSES QUE JÁ VIMOS DESDE O INICIO DO ESTUDO 
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É 
"""

c1 = Cliente('Romullo', 37)  # Neste exemplo a classe Cliente herda os métodos da super classe como foi passado por
# parâmetro a classe Pessoa em Cliente mais essa classe não pode acessar a classe Aluno porque o não pertence
# print(c1.nome)
c1.falar()
c1.comprar()

a1 = Aluno('Ludmilla', 7)  # Neste exemplo a classe Aluno herda os métodos da super classe como foi passado por
# parâmetro a classe Pessoa em Aluno mais essa classe não pode acessar a classe Pessoa porque o não pertence
# print(a1.nome)
a1.falar()
a1.estudar()

p1 = Pessoa('João', 43)  # Neste exemplo a class Pessoa não pode acessar a classe nem Cliente e nem Aluno ele não
# herda nada das classes
p1.falar()