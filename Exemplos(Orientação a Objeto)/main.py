# from pessoa import Pessoa # chamando o arquivo pessoa.py usando o exemplo normal de instânciar a class
from pessoaMethod import Pessoa  # chamando o arquivo pessoaMethod.py e usando o exemplo do @classmethod
from produto import Produto
from atributoClasse import A
from publicProtectedPrivate import BaseDeDados

"""Trabalhando com classe"""

p1 = Pessoa('Romullo', 37)
# p1.comer('pizza')
# p1.falar('POO')
# p1.parar_comer()
# p1.falar('POO')
# p1.comer('alimento')

p2 = Pessoa('Luiz', 33)
# p1.falar('POO')
# p2.comer('sorvete')
# p1.comer('churrasco')

# print(p2.get_ano_nascimento())

# print(p1)
# print(p1.nome, p1.idade)
# p1.get_ano_nascimento()
# print(Pessoa.gera_id())
# print(p1.gera_id())


"""Usando Getters e Setters """

# p1 = Produto('Camiseta', 50)
# p1.desconto(10)
# print(p1.nome, p1.preco)

""" Se o valor da caneca vim em formato de string ocorrerá um erro por exemplo 'R$15' se alguém setar esse valor"""
# p2 = Produto('Caneca', 'R$15')
# p2.desconto(10)
# print(p2.nome, p2.preco)


"""Exemplo usando o atributos da classe"""

# a1 = A()
# a2 = A()
#
# print(a1.vc)
# print(a2.vc)
# print(A.vc)

"""Trabalhando com class public, protected, private"""

# bd = BaseDeDados()
# bd.inserir_cliente(1, 'Romullo')
# bd.inserir_cliente(2, 'Isaura')
# bd.inserir_cliente(3, 'Ludmilla')
# bd.inserir_cliente(4, 'Maria ')
# bd.apaga_cliente(4)
# bd.__dados = 'Outra coisa'
# print(bd.__dados) # Acessando o private mais não alterando o atributo da classe
# print(bd._BaseDeDados__dados) # Acessando o private da classe
# bd.lista_clientes()
# print(bd.dados) # Dessa maneira podemos acessar a o atributo da classe com o decorator da função
# passando o property da classe é criando setter para passar as informações para ser alterados.