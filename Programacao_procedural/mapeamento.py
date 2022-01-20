from dados import produtos, pessoas, lista


"""Nesse caso estamos pegando a lista de dados.py
e Multiplicando por 2, usamos a função map, a anônima lambda como x
e pedimos para multiplicar o x por 2. A função map retornará um iterador"""

nova_lista = map(lambda x: x * 2, lista)

print(nova_lista)  # <map object at 0x0073EBF8>
print(list(nova_lista))  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

nova_lista1 = [x * 2 for x in lista]

print(nova_lista1)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# Para printar apenas os preços

precos = map(lambda p: p['preco'], produtos)

for preco in precos:
    print(preco)

# Aumentar 5% dos valores em todos preços e retornar o dicionário:
# Usamos o round para arredondar/limitar as casas decimais, e selecionamos 2 no caso, no fim da função.
# o "p" no caso se refere aos preços
# Após a função usamos o map, sinalizamos a função e a variável a ser aplicada.

def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05,2)
    return p

novos_produtos = map(aumenta_preco, produtos)

for produto in novos_produtos:
    print(produto)

# Para retornar apenas o nome em pessoas:

for pessoa in pessoas:
    print(pessoa)

nomes = map(lambda p: p['nome'], pessoas)

for pessoa in nomes:
    print(pessoa)

# Para aumentar uma porcentagem de idade para todas as pessoas:

def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20, 2)
    return p

idades = map(aumenta_idade, pessoas)

for idade in idades:
    print(idade)
