class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_endereco(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):  # Usando essa função __del__ ele informa que depois de usarmos a classe ele irá apagar da
        # memória onde os dados estão armazenados
        print(f'{self.nome} FOI APAGADO')

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):  # Usando essa função __del__ ele informa que depois de usarmos a classe ele irá apagar da
        # memória onde os dados estão armazenados
        print(f'{self.cidade}/{self.estado} FOI APAGADO')