"""
A partir do momento que setamos o valor do simbolo na função
devemos setar os próximos também, ou dará erro.

Args - arguments
Kwargs - Key word arguments
"""

def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5, nome, a6)
    return nome, a6

# var = func(1,2,3,4,5, nome='Maria', a6='5')
# print(var)  # ('Maria', '5')
#
# def func(*args):
#     args = list(args)
#     print(args)
#     print(args[0])
#     print(args[-1])
#     print(len(args))
#
# lista = [1,2,3,4,5]
# n1, n2, *n = lista
# print(n1, n2, n)
# print(*lista, sep='-')

def func(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])

    idade = kwargs.get('nome')
    if idade is not None:
        print(idade)
    else:
        print('Não existe')

lista = [1,2,3,4,5,6]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, nome='Luiz', sobrenome='Miranda') # asterisco desempacota a lista.
