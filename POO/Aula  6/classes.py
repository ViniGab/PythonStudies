

class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        # Para fazer a associação criamos a variável abaixo com o None
        # E ali abaixo fizemos o getter/setter para poder utiliza-lá, pois a mesma está privada.
        # O exemplo com a associação está no associacao.py

        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo...')

class MaquinaDeEscrever:
    def escrever(self):
        print('Máquina está escrevendo...')