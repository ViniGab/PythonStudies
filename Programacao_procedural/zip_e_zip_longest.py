from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']
estados = ['SP', 'MG', 'BA']

"""Com o zip longest, agora o Monte Belo em conjunto com estados fica com o 
None sinalizado, pois não foi incluído. No caso do fillvalue ele vai acrescentar
a palavra/elemento desejado aos locais sem valor(None), como nos locais onde a siga
dos estados está ausente."""

# cidades_estados = zip_longest(indice, estados, cidades, fillvalue='Estado')
cidades_estados = zip(indice, estados, cidades)

for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)  # Desempacotando a tupla tripla.

"""
0 SP São Paulo
1 MG Belo Horizonte
2 BA Salvador
"""