from classes import Cliente

cliente1 = Cliente('Romullo', 37)
cliente1.insere_endereco('São Paulo', 'SP')
print(cliente1.nome)
cliente1.lista_endereco()
# del(cliente1) # Usando este del ele exibe o primeiro print que foi os dados inseridos e logo depois esse del
# informa o que foi inserido foi apagado da memória
print()

cliente2 = Cliente('Meire', 55)
cliente2.insere_endereco('São Vicente', 'SP')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_endereco()
# del(cliente2) # Usando este del ele exibe o primeiro print que foi os dados inseridos e logo depois esse del
# informa o que foi inserido foi apagado da memória
print()

cliente3 = Cliente('Zilda', 75)
cliente3.insere_endereco('Itabuna', 'BA')
print(cliente3.nome)
cliente3.lista_endereco()
# del(cliente3) # Usando este del ele exibe o primeiro print que foi os dados inseridos e logo depois esse del
# informa o que foi inserido foi apagado da memória
print()

print('##########################################')

print()
