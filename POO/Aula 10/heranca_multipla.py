

class A:
    def falar(self):
        print('Falando... Estou em A.')

class B(A):
    def falar(self):
        print('Falando... Estou em A.')

class C(A):
    def falar(self):
        print('Falando... Estou em B.')

class D(B, C):
    pass

"""Como B foi referenciado primeiro ele vai procurar o método primeiro em B,
Caso B não tenha o método ele vai procurar em C."""

d = D()
d.falar()

###################################################

from smartphone import Smartphone

smartphone = Smartphone('Pocophone F1')
smartphone.conectar()
smartphone.desligar()
smartphone.ligar()
smartphone.conectar()
smartphone.conectar()
smartphone.conectar()
smartphone.desligar()
smartphone.conectar()
smartphone.desconectar()
smartphone.desconectar()