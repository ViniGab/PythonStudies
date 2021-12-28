"""
Contadores e acumuladores.
"""

# Laço while precisa de um número que no caso é o contador.
# Acumuladores são acrescentados a cada laço.

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no 10 ;) ')