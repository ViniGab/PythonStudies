# def funcao(var):
#     return var
#
# variavel = funcao('Valor que eu quero')
# print(variavel)  #None representa um não valor


def divisao(n1, n2):
    if n2 == 0:  # Caso tentem realizar divisao por 0.
        return

    return n1 / n2

divide = divisao(8, 4)
print(divide)

if divide:
    print(divide)
else:
    print('Conta inválida.')

def dumb():
    return 1.1

print(dumb(), type(dumb()))  # o type será o sinalizado em return.

def tuple():
    return ('Luiz', 'Maria')

var = tuple()

print(var[0], type(var))