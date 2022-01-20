from dados import produtos, pessoas, lista
from functools import reduce

acumula = 0
for item in lista:
    acumula += item

print(acumula)

# Aqui abaixo passamos um acumulador(ac) e o item(i).
# Passamos também a variável lista no caso e o início que sera 0

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)  # 55

# Aqui temos a soma dos preços com o acumulador.

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos)  # 298.68999999999994

# Podemos verificar a média com a operação acima também, usando:

print(soma_precos / len(produtos))  # 29.868999999999993

soma_idades = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(soma_idades)  # 309
print(soma_idades / len(pessoas))  #30.9
