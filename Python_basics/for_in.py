# Diferente do while, o laço for nós utilizamos para coisas finitas.

texto = 'Python'

"""
Geralmente o laço while não é utilizado para essa operação abaixo, usamos o for, pois fica menos complexo:

c = 0
while c < len(texto):
    print(texto[c])
    c +=1
"""

for letra in texto:  # A palavra/dígito para a iteração não precisa ser "letra", pode ser quase qualquer coisa.
    print(letra)

for n, letra in enumerate(texto):
    print(n, letra)  # para ter o contador no for, podemos usar o enumerate com um contador.

for x in range(10):  # a range recebe os três parâmetros, start, stop, step.
    print(x)

for n in range(100):  # Até 100 de 8 em 8.
    if n % 8 == 0:
        print(n)

nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

        print(nova_string)

