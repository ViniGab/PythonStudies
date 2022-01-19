"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

# Para saber as combinações possíveis, todas combinações possíveis:

for grupo in product(pessoas, repeat=2):  # Em grupo de dois.
    print(grupo)

print('Aqui o próximo:')

for grupo in combinations(pessoas, 3): # Em grupo de três.
    print(grupo)