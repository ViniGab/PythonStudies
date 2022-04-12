"""
Javascript Object Notation - JSON
JSON é um formato de troca de dados entre sistemas
muito leve e de fácil utilização. Muito utilizado por APIS
"""
from dados import *
import json

# Transformando a lista dos clientes_dicionario localizada em dados em Json.
# O ident é para melhor vizualização dos dados.

dados_json = json.dumps(clientes_dicionario, indent=4)
print(dados_json)

# Transformando um arquivo json em dicionário novamente

print(clientes_json)
dicionario = json.loads(clientes_json) # Feito

for chave, valor in dicionario.items():
    print(chave)
    print(valor)

# Criando o dicionário em arquivo com formato Json (clientes.json).

with open('clientes.json', 'w') as arquivo:
    json.dump(clientes_dicionario, arquivo, indent=4)

with open('clientes.json', 'r') as arquivo:
    dados = json.load(arquivo)

print(dados)