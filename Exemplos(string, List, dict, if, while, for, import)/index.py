# Comandos para iniciar o projeto no terminal -> python3 -m venv venv
# Após executar o comando devemos fazer rodar o venv no projeto usamos o comando no terminal -> source venv/bin/activate

# nome = "Romullo"
# idade = 36
# peso = 80.5
# e_programador = True

# No print "f" significa formatar a mensagem por isso que usamos {} com o nome da variável dentro das chaves
# print(f"Olá {nome}, você tem {idade} anos e pesa {peso} Kg")

# Todos os valores que vem do input vem no formato de String devemos converter caso for fazer cálculos

# nome = input("Digite o seu nome:")

# print(f"Olá {nome}, tudo bem!")

# print(type(nome), type(idade))

"""
nota1 = int(input('Digite a nota 1:'))
nota2 = int(input('Digite a nota 2:'))

# operador = nota1 % nota2
media = (nota1 + nota2) / 2

print(f"O resultado é {media}")
"""

# operador = 5 > 5
# operador = not True
# print(operador)

# media = int(input("Digite sua média: "))
#
# if media >= 6:
#     print("Você passou de ano")
# else:
#     print("Reprovado")
#

# nota1 = int(input("Digite a nota 1: "))
# nota2 = int(input("Digite a nota 2: "))
#
# media = (nota1 + nota2) / 2
#
# print(media)
#
# if media >= 6:
#     print("Aprovado")
# elif media < 6 and media >= 4:
#     print("Recuperação")
# else:
#     print("Reprovado")

# n = 0
#
# while n < 10:
#     print(n)
#     n = n + 1

"""Fazendo uma taboada com while"""

# n = 1
# tab = 1
#
# while tab <= 10:
#     while n < 11:
#         if n == 6:
#             break
#         """break para o processo do while mesmo se a condição ainda estiver em andamento como nesse exemplo"""
#         resposta = n * tab
#         print(f"{tab} x {n} = {resposta}")
#         n += 1
#     n = 1
#     tab += 1
#     print("------------------")
#

"""Fazendo o laço de repetição usando o for"""

# for i in range(101):
#     if i % 2 != 0:
#         print(i)

# for i in range(1, 11):
#     for x in range(1, 11):
#         resultado = i * x
#         print(f"{i} x {x} = {resultado}")
#     print("---------")


"""Listas"""
# idades = [21, 22, 50, 60]
# print(idades)
#
# idades.pop() # remove o último elemento do array se passarmos um valor dentro do (1) parenteses irá excluir a posição do elemento informado
#
# print(idades)

"""Calcular a média de uma sala"""

# notas = [10, 5, 8, 9, 4, 3, 0]
# media = 0
# mediaSala = 0
# aprovados = 0
# reprovados = 0
#
# for i in notas:
#     media += int(i)
#     if i >= 6:
#        aprovados = aprovados + 1
#     else:
#         reprovados = reprovados + 1
#
# mediaSala = int(media / len(notas))
#
# print(f"A Média da sala foi {mediaSala}")
# print(f"Alunos aprovados {aprovados}")
# print(f"Alunos reprovados {reprovados}")

# notas = []
#
# while True:
#     nota = int(input('Digite uma nota ou -1 para sair'))
#     if nota == -1:
#         break
#     notas.append(nota)
#
# soma = 0
# for i in notas:
#     soma = soma + i
#
# media = soma / len(notas)
#
# print(media)

"""Usando dicionários"""

# pessoa = {'nome': 'Romullo',
#           'idade': 37,
#           'cidade': 'São Paulo'}
#
# pessoas = [{'nome': 'Ludmilla', 'idade': 7, 'cidade': 'São Paulo'},
#            {'nome': 'Isaura', 'idade': 34, 'cidade': 'São Paulo'},
#            {'nome': 'Luzia', 'idade': 76, 'cidade': 'Minas Gerais'}]
# idades = 0
# for i in pessoas:
#     idades = idades + int(i['idade'])
# print(idades)

"""Usando função"""


# def exibe_bom_dia():
#     print('Bom dia!')
#     print('Tudo bem?')
#
# exibe_bom_dia()
#
# def soma(n1, n2):
#     resultado = n1 + n2
#     return resultado
#
# soma_total = soma(5,7)
#
# print(f"A soma do valor é: {soma_total}")

"""trabalhando com Importação usando o arquivo calculo.py como exemplo"""

# import calculos
# como no exemplo acima esse tipo de import nos importamos tudo que contém no arquivo como funções e variáveis
# para ser chamado devemos fazer dessa forma
# print(calculos.x)
# devemos fazer dessa maneira usar calculos. o nome da função ou variavel que queremos usar

from calculos import soma, y
# como no exemplo acima nos expecificamos o que queremos que seja importado, como no exemplo é a função soma
# também podemos passar outras importações como fix com o y especificando qual informação eu

print(f"O valor somado é: {soma(5, 22)}")
print(y)

