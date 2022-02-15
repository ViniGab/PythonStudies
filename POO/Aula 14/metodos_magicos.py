# Os métodos mágicos começam com dois underline e terminam com dois underline.
# Modificam o comportamento da classe.

# https://rszalski.github.io/magicmethods/

class A:

    def __new__(cls, *args, **kwargs):
        #return super().__new__(cls)
        return object.__new__(cls)

    def __init__(self):
        print('Eu sou o INIT')  # Inicializador.



a = A()  #Eu sou o INIT
print(type(a))  # <class '__main__.A'>

# Puta aula chata volto dps.