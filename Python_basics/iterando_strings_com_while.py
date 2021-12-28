frase = 'O rato roeu a roupa do rei de roma.'
tamanho_frase = len(frase)
print(tamanho_frase)

contador = 0

# while contador < 10:
#     print(contador)
#     contador += 1

# while contador < 10:
#     print(frase[contador], contador)
#     contador += 1

# O 0
#   1
# r 2
# a 3
# t 4
# o 5
#   6
# r 7
# o 8
# e 9

# while contador < tamanho_frase:
#     print(frase[contador], contador)
#     contador += 1

nova_string = ''

input_do_usuario = input('Qual letra deseja colocar maiúscula? ')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)  # O Rato Roeu a Roupa do Rei de Roma.
