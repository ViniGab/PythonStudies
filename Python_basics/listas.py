"""
Listas em Python
"""

lista = ['A', 'B', 'C', 'D', 'E']


print(lista[0:3])  # ['A', 'B', 'C']
print(lista[2:])  # ['C', 'D', 'E']
print(lista[-1])  # O último da lista. E


l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2
print(l3)  # [1, 2, 3, 4, 5, 6]
l3.append('B')  #append acrescenta valores.
print(l3)  # [1, 2, 3, 4, 5, 6, 'B']
l3.insert(2, 'Lagoa')  #com o insert escolhemos a posição onde a inclusão será realizada.
print(l3)  # [1, 2, 'Lagoa', 3, 4, 5, 6, 'B']
l3.pop()  # pop retira o último elemento ou o selecionado na lista(0,1,2,3...)
print(l3)  # [1, 2, 'Lagoa', 3, 4, 5, 6]
del(l3[3:5])  # deleta mais de um elemento da lista.
print(l3)  # [1, 2, 'Lagoa', 5, 6]


#Convertendo range em lista. No caso objetos iteráveis podem ser convertidos em lista.
l4 = list(range(1, 10))
print(l2)

l4 = list(range(1,10))
print(l4)

for valor in l4:
    print(valor)

l5 = ['String', True, 10, -20.5]

for elem in l2:
    print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')

