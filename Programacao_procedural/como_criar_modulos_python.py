# Esse python file foi para aprender a criar um módulo
# Este será usado em outros locais(no caso  app.py)
import math

PI = math.pi

def dobra_lista(lista):
    return [x*2 for x in lista]

def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r


# O pessoal geralmente usa isso para4 caso for importado em outro módulo não ser executado.

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print(dobra_lista((lista)))
    print(multiplica(lista))
    print(PI)

