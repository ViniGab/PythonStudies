
nome = input('Qual o seu nome? ')

# if nome:
#     print(nome)
# else:
#     print('Você não digitou nada.')

# para simplificar a situação acima.

print(nome or None or False or 0 or 'Você não digitou nada!')

a = 0  # False
b = None  # False
c = False  # False
d = []  # False
e = {}  # False
f = 22  # True
g = 'Luiz'  # True

