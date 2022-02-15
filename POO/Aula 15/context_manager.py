"""Senpre que queremos abrir/fechar alguma coisa usamos o
gerenciador de contexto"""

# arquivo = open('abc.txt', 'w')
# arquivo.write('Alguma coisa')
# arquivo.close()

"""
Esse método serve para basicamente qualquer coisa que você tenha que abrir e depois fechar,
É viável pois não deixa arquivos abertos acidentalmente, sendo este o gerenciador de contexto."""


class Arquivo:
    def __init__(self, arquivo, modo):
        print('Abrindo arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('Retornou arquivo.')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('fechando arquivo.')
        self.arquivo.close()


with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa')


from contextlib import contextmanager

# Com o import acima não preciso usar a classe

# Outra maneira de criar o gerenciador.

@contextmanager
def abrir(arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()

with abrir('abc.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')

# lembrando que após criar o gerenciador temos que usar o "with" para funcionar com o exit.
