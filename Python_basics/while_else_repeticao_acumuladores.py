"""
Contadores e acumuladores.
"""

# Laço while precisa de um número que no caso é o contador.
# Acumuladores são acrescentados a cada laço.

# contador = 1
# acumulador = 1
#
# while contador <= 10:
#     print(contador, acumulador)
#
#     acumulador = acumulador + contador
#     contador += 1
# else:
#     print('Cheguei no 10 ;) ')

vendas_de_bananas = 0
bananas_vendidas = 0

while vendas_de_bananas <= 50:
    print(vendas_de_bananas, bananas_vendidas)

    bananas_vendidas = bananas_vendidas + vendas_de_bananas
    vendas_de_bananas += 1
else:
    print('Bati a meta de vendas.')
