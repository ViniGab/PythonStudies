
lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]

d1 = {x: y*2 for x, y in lista}

print(d1)  # {'chave': 'valorvalor', 'chave2': 'valor2valor2'}

d1 = {x.upper(): y.upper() for x, y in lista}
print(d1)  # {'CHAVE': 'VALOR', 'CHAVE2': 'VALOR2'}

