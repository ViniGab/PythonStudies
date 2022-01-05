# Desempacotamento:

lista = ['Luiz', 'João', 'Maria']

n1, n2, n3 = lista

print(n2)  #'João'

# É possível utilizar o desempacotando com asterisco para o restante da lista:

p1, *outra_lista = lista

print(*outra_lista) # João Maria

*início_lista, p2, p3 = lista

print(início_lista)  #['Luiz']
