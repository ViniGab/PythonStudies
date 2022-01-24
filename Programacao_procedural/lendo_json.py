# Retornar o arquivo JSON para o dicionário.

with open('abc.txt', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)
    print(d1_json)