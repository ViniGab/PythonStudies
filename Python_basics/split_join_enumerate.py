"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos iteráveis
"""

string = "O Brasil é o país do futebol, O Brasil é penta."
lista_1 = string.split(' ')  # Cria lista com o elemento selecionado de dentro, no caso deste, o espaço.
lista_2 = string.split(',')
print(lista_1)  # ['O', 'Brasil', 'é', 'o', 'país', 'do', 'futebol,', 'O', 'Brasil', 'é', 'penta.']
print(lista_2)  # ['O Brasil é o país do futebol', ' O Brasil é penta.']

# for valor in lista_1:
#     print(valor)
#
# for valor in lista_2:
#     print(valor)
#
# for valor in lista_1:
#     print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase.')

palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

lista = string.split(' ')  # ['O', 'Brasil', 'é', 'o', 'país', 'do', 'futebol,', 'O', 'Brasil', 'é', 'penta.']


print(lista)

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])

lista3 = [
    [1,2],
    [3,4],
    [5,6],
]

for v in lista3:
    print(v[0])  # imprime 1, 3 e 5 em linhas diferentes.

for v in lista3:
    print(v[0], v[1])  # imprime tudo

lista4 = ['luiz', 'João', 'Maria']
n1, n2, n3 = lista4
print(n2)  # João por desempacotamento.