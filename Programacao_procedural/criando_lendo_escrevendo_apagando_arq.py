# http://docs.python.org/3/library/functions.html#open
import os
import json

# Abrir um arquivo para escrita, no caso do w+ é para sinalizar que podemos ler e escrever.
# A diferença de a+ para w+ é que o a+ é append, adiciona, o w+ apaga e sobrescreve os arquivos no local.

file = open('abc.txt', 'w+')

# Para escrever coisas no arquivo.

file.write('Linha1\n')
file.write('Linha2\n')
file.write('Linha3\n')

# file.seek é para voltar o cursor ao início do arquivo.

file.seek(0, 0)
print('Lendo linhas:')
print(file.read())
print('#############')

file.seek(0, 0)

# Lendo linha por linha.
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')

# readlines no plural como o próprio nome já explicita é com mais de uma linha.

file.seek(0, 0)
for linha in file.readlines():
    print(linha)

# É importante sempre fechar o arquivo após o uso para não gerar erros posteriores.

file.close()

# Jeito mais "Pythonico" de fazer.

with open('abc.txt', 'w+') as file:
    file.write('Linha1\n'),
    file.write('Linha2\n'),
    file.write('Linha3\n'),

    file.seek(0)
    print(file.read())

# Para apagar o arquivo importamos o os e fazemos o seguinte:

# os.remove('abc.txt')

# Para fazer o arquivo JSON importamos o Json e fazemos o seguinte:

d1 = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': 25,
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 30,
    },
}

d1_json = json.dumps(d1)
print(d1_json)

