# add (adiciona), update (atualiza, clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)


# Primeira maneira de criar o set.
# A diferença entre o set e dicionário é que o set tem apenas valores.
# No set suporta apenas elementos imutáveis.

s1 = {1,2,3,4,5}

print(s1)

# É iterável.

for v in s1:
    print(v)

# Outra maneira de criar sets.

s2 = set()
s2.add(1)
s2.add(2)
s2.add((1,2,3,'Luiz'))

print(s2)  # {1, 2, (1, 2, 3, 'Luiz')}

# Podemos utilizar o  update também, porém ele itera sobre cada elemento se for incluído mais de um.

s2.update('Python')

print(s2)  # Olha como ficou a inclusão "'y', 'n', 't', 'o', 'h', 'P'}"

# O set não aceita elementos duplicados. Portanto podemos usar para eliminar elementos duplicados.

l1 = [1,2,3,4,1,1,21,3,2,3,21,1,1,1,2,3,4,5,1,21,6, 'Maria', 'Maria']
l1 = set(l1)

print(l1)  # {1, 2, 3, 4, 5, 6, 'Maria', 21}

# E retornamos para lista, porém os elementos voltam fora de ordem.

l1 = list(l1)

# Para acessar o último elemento da lista

print(l1[-1])

# Podemos usar o union ou o | para juntar os sets, lembrando que não podem ter duplicados.

f1 = {1,2,3,4,5}
f2 = {1,2,3,4,5,6}
f3 = f1 | f2

print(f3)  # {1, 2, 3, 4, 5, 6}

# Para localizar a intersection (elementos que estão nos dois sets) usamos o &.

f1 = {1,2,3,4,5}
f2 = {1,2,3,4,5,6}
f3 = f1 & f2

print(f3)  # {1, 2, 3, 4, 5}

# Para pegar a diferença, usamos o sinal de -, para pegar os sets que estão diferentes, a ordem importa.

f1 = {1,2,3,4,5,7}
f2 = {1,2,3,4,5,6}
f3 = f1 - f2  # {7}
f3 = f2 - f1  # {6}

# Para pegar a diferença simétrica, que está nos dois, usamos o ^.

f4 = {1,2,3,4,5,7}
f5 = {1,2,3,4,5,6}
f6 = f4 ^ f5
print(f6)  # {6, 7}






