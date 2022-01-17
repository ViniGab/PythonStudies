# Expressão padrão:

def funcao(arg, arg2):
    return arg * arg2

var = funcao(2,2)
print(var)

# Agora da maneira Lambda:

a = lambda x, y: x * y

print(a(2,2))

lista = [
    ['P1', 13],
    ['P1', 6],
    ['P1', 7],
    ['P1', 50],
    ['P1', 8],
]


lista2 = [
    ['P1', 54],
    ['P1', 44],
    ['P1', 6],
    ['P1', 13],
    ['P1', 31],
]
# Não altera pois existem listas dentro das outras listas, então podemos fazer assim.
# Essa é a maneira com função normal.

def func(item):
    return item[1]

lista.sort(key=func,reverse = True) #Caso queiramos reverter também, podemos utilizar o reverse = True
print(lista)

# Agora com função lambda:

lista2.sort(key=lambda item: item[1])
print(lista2)

# Outra maneira com lambda:

print(sorted(lista, key=lambda i: i[1]))  # Também podemos organizar assim.