"""Atributos da classe"""


class A:
    vc = 123

    def __init__(self):
        self.vc = 321
        # pass


A.vc = 'Alterado' # dessa forma ele está alterando o atributo da classe

# Para eu alterar o valor do atributo da classe devemos chamar como no exemplo abaixo
# A.vc = 321

# Quando a classe A e chamada ele olha primeiro na instância da classe que é a função construtora __init__ passando self
