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