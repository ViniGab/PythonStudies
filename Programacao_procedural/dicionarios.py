import copy

# Dicionário = chave e valor.
import copy

d1 = {'chave1':'valor da chave'}
d1['nova_chave'] = 'Valor da nova chave'

print(type(d1))
print(d1)

# Outra forma de criar dicionário, com dict.

d2 = dict(chave1='Valor da chave', chave2='Valor da outra chave')
print(d2)

# As chaves precisam ser nominalmente diferentes.

d3 = { 'Chave1' : 'valor1','chave2' : 'valor2'}

d4 = {
    'chave1': 'valor',
    'chave2': 'Outro valor',
    'chave3': 'Tupla',
}

print(d4[('chave3')])  # Tupla

# Podemos fazer busca com o get também:

print(d1.get('nomedachave'))  # Como não existe retorna None, não crashando o código.


# Alterando a chave com update.

d1.update({'nova_chave':'novo_valor_com_update'})

print(d1)

# A função len conta os pares do dict.

print(len(d4))  #3

# Para iterar as chaves

for k in d4:
    print(k)

# Para iterar os valores

for v in d4.values():
    print(v)

# Para iterar os dois utilizamos o items:

for k in d4.items():
    print(k[0], k[1])

# Assim também:

for k, v in d4.items():
    print(k, v)

clientes = {
    'cliente1' : {
        'nome' : 'Luiz',
        'sobrenome': 'Otávio',
    },
    'cliente2' : {
        'nome' : 'João',
        'sobrenome': 'Moreira',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

# Os dois locais abaixo apontam para o mesmo local, para mexer nos mesmos usamos uma shallow copy.copy:

t1 = {1: 'a', 2: 'b', 3: 'c', 'd' : ['Luiz', 'Otávio']}
v = t1

v[1] = 'Luiz'

print(t1)
print(v)

# Deep copy necessário colocar o import copy

copia = copy.deepcopy(t1)
print(copia)

copia[1] = 'Luiz'
copia['d'][0] = 'Joãozinho'


if copia == t1:
    print('É igual.')
else:
    print('Não é igual')
