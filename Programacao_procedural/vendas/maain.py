from calc_preco import *
from formata import preco


preco1 = 49.90
preco_com_aumento = aumento(valor=preco1, porcentagem=15, formata=True)
print(preco_com_aumento)

preco2 = 49.90
preco_com_reducao = reducao(valor=preco2, porcentagem=15, formata=True)
print(preco_com_reducao)

preco(21.5)