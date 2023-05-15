"""
public, protected, private

_ privado/protected ( _public )-> underline você coloca os atributos da classe em protected, mais ele pode ser acessado para ser utilizado quando a classe é chamada
como exemplo _dados podendo ser acessado bd._dados

__ private (_NOMECLASSE__nomeatributo) -> dois underline deixa extremamente seguro a classe, para acessa-lo devemos chamar a classe bd._BaseDeDados__dados, dessa forma você consegue
acessar o atributo da classe, se for chamado como neste exemplo aqui bd.__dados ele cria outra instância e passa para o dados, mais não é alterado no
classe BaseDeDados, veja no exemplo.

__ private -> OBS também é possível proteger os métodos como exemplo def __inserir_cliente(self):
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

