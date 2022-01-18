# São usadas para otimização/perfomance e escrever menos linhas.

l1 = [1,2,3,4,5,6,7,8,9]
l2 = [variavel for variavel in l1]

print(l2)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Para multiplicar por 2.

ex2 = [v * 2 for v in l1]  # [2, 4, 6, 8, 10, 12, 14, 16, 18]

print(ex2)


# Para criar uma tupla.

ex3 = [(v, v2) for v in l1 for v2 in range(3)]

print(ex3)  # [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2), (6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2), (9, 0), (9, 1), (9, 2)]


# Para trocar elementos

l3 = ['Luiz', 'Mauro', 'Maria']
ex4 = [v.replace('a', '@')for v in l3]
print(ex4)  # ['Luiz', 'M@uro', 'M@ri@']

# Para inverter chave e valor

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)

ex5 = [(y, x) for x, y in tupla]
print(ex5)  # [('valor', 'chave'), ('valor2', 'chave2')]


# Para saber os números da lista divisíveis por 3 e 8.

l4 = list(range(100))
print(l4)
ex6 = [v for v in l4 if v % 3 == 0 if v % 8 == 0]
print(ex6)  # [0, 24, 48, 72, 96]


# Usando a mesma situação acima, mas com else:

ex7 = [v if v % 3 == 0 else 'No' for v in l4]
print(ex7)  # [0, 'No', 'No', 3, 'No', 'No', 6, 'No', 'No', 9, 'No', 'No', 12, 'No', 'No', 15, 'No', 'No', 18, 'No', 'No', 21, 'No', 'No', 24, 'No', 'No', 27, 'No', 'No', 30, 'No', 'No', 33, 'No', 'No', 36, 'No', 'No', 39, 'No', 'No', 42, 'No', 'No', 45, 'No', 'No', 48, 'No', 'No', 51, 'No', 'No', 54, 'No', 'No', 57, 'No', 'No', 60, 'No', 'No', 63, 'No', 'No', 66, 'No', 'No', 69, 'No', 'No', 72, 'No', 'No', 75, 'No', 'No', 78, 'No', 'No', 81, 'No', 'No', 84, 'No', 'No', 87, 'No', 'No', 90, 'No', 'No', 93, 'No', 'No', 96, 'No', 'No', 99]

