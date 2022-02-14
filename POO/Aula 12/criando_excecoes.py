# Criando a exceção e tratando o erro com a mesma, bem simples.


class TaErradoError(Exception):
    pass

def testar():
    raise TaErradoError('Errado!')

try:
    testar()
except TaErradoError as error:
    print(f'Erro: {error}')