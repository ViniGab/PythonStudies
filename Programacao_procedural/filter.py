from dados import produtos, pessoas,  lista

# A função filter vai retornar de acordo com True ou False para os dados que você passar:

nova_lista = filter(lambda x: x > 5, lista)
print(nova_lista)  # <filter object at 0x0044EBF8>
print(list(nova_lista))  # [6, 7, 8, 9, 10]

# Podemos realizar a mesma condição acima com o list comprehension

nova_lista_comprehension = [x for x in lista if x > 5]
print(list(nova_lista_comprehension))  # [6, 7, 8, 9, 10]

# Podemos escolher os produtos com os preços desejados a serem filtrados também.

maior_preco = filter(lambda p: p['preco'] > 50, produtos)

for produto in maior_preco:
    print(produto)

# Caso a gente utilize em mais de um local a mesma situação podemos usar uma função também.
# Trazendo o mesmo resultado da operação realizada acima:

def filtra(produto):
    if produto['preco'] > 50:
        produto['é_caro'] = True
        return True

maior_preco2 = filter(filtra, produtos)

for produto in maior_preco2:
    print(produto)

# Para filtrar pessoas com determinada idade.

def filtro_idade(pessoa):
    if pessoa['idade'] < 18:
        return True

new_list = filter(filtro_idade, pessoas)

for idade in new_list:
    print(idade)