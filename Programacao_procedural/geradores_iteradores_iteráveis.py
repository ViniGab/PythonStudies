import sys
import time

lista = [0,1,2,3,4,5]
lista = iter(lista)

"""O objeto iteravel não necessariamente vai te dar um elemento por vez,
 já no caso do iterador, ele da o elemento passo a passo. Fiz o lista = iter(lista) acima
 , por isso ele virou um iterador, mas antes disso não era. Observe a situação abaixo"""


print(next(lista))  # 0
print(next(lista))  # 1
print(next(lista))  # 2
print(next(lista))  # 3

# Para saber se o elemento é iterável.

print(hasattr(lista, '__iter__'))  # True


# Para saber se o elemento é um iterador

print(hasattr(lista, '__next__'))  # False mas como foi feito iter agora é.

"""O objeto iteravel não necessariamente vai te dar um elemento por vez,
 já no caso do iterador, ele da o elemento passo a passo. Fiz o lista = iter(lista) acima
 , por isso ele virou um iterador, mas antes disso não era. Observe a situação abaixo"""

# Para verificar o tamanho da lista.

list4 = list(range(10))  # 24 bytes


print(sys.getsizeof(lista))  # 24 bytes

# Para transformar a função abaixo em um gerador, mostrando um número de cada vez:

# def gera():
#     r = []
#     for n in range(100):
#         r.append(n)
#         time.sleep(0.1)
#     return r

def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)

g = gera()

print(g)  # <generator object gera at 0x0036CAE0>

for v in g:
    print(v)

"""Na situação abaixo a cada next que damos veremos uma das variavel1 diferentes
pois o mesmo é iterável e iterador."""

def gera1():
    variavel1 = 'Valor1'
    yield variavel1
    variavel1 = 'Valor2'
    yield variavel1
    variavel1 = 'Valor3'
    yield variavel1

f = gera1()

print(next(f))
print(next(f))
print(next(f))

lista1 = [x for x in range(100)]
lista2 = (x for x in range(100))

listinha = list(range(100))

print(sys.getsizeof(listinha))  # 428
print(sys.getsizeof(lista1))  #  452
print(sys.getsizeof(lista2))  #  56


