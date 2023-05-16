from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
#
# print(escritor.nome)
# print(caneta.marca)
# maquina.escrever()

escritor.ferramenta = caneta  # O que está sendo executado aqui é passar o conteudo inteiro da classe MaquinaDeEscrever
# para a instância da classe ferramenta ele vai ser armazenado na memória onde será chamado no exemplo abaixo

escritor.ferramenta.escrever()  # Após ter sido passado para a instância da classe ferramenta o método escrever() no
# caso a função, ele será chamado
