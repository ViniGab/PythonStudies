from itertools import groupby

alunos = [
    {'nome': 'Carlos', 'nota': 'A' },
    {'nome': 'Henrique', 'nota': 'B' },
    {'nome': 'Ricardo', 'nota': 'B' },
    {'nome': 'Maria', 'nota': 'C' },
    {'nome': 'Kaio', 'nota': 'A' },
    {'nome': 'Joana', 'nota': 'B' },
    {'nome': 'Letícia', 'nota': 'C' },
    {'nome': 'João', 'nota': 'A' },
    {'nome': 'Luana', 'nota': 'C' },
    {'nome': 'Luiz', 'nota': 'B' },
]

# Para ordenar as notas com o groupby:


ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}')
    for aluno in valores_agrupados:
        print(aluno)
    print()