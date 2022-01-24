# Módulos padrão do Python:
# Módulos são arquivos .py (que contém código Python) e servem para expandir
# as funcionalidades padrão da linguagem.
# Veja todos os modulos padrão do python em:
# https://docs.python.org/3/py-modindex.html

import sys

print(sys.platform)

# Podemos usar assim também e dar um nome para ser retornado

from sys import platform as so

print(so)

import random

for i in range(10):
    print(random.randint(0,10))

# Podemos importar tudo do módulo com o *

from random import *

# Esse modulo instalei usando o pip install pymysql no terminal.

import pymysql