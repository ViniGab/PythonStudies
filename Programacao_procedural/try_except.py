"""Para trabalhar com exceções incluímos o try/excep no bloco, assim como
usamos o "if" e etc"""

# O que tentarmos rodar no bloco try ele tenta rodar e caso não ocorra sucesso ele vai pro except
try:
    print(a)
except NameError as erro:
    print('Error', erro)



print('Bora continuar...')

# Caso ocorra um erro logo no except usamos o except Exception.
try:
    a = []
    print(a[1])
except NameError as erro:
    print('Error', erro)
except Exception as erro:
    print('Ocorreu um erro inesperado.')  # Ocorreu um erro inesperado.

# Tratando o caso acima como IndexError:

try:
    a = []
    print(a[1])
except NameError as erro:
    print('Error', erro)
except IndexError as erro:
    print('Erro de índice.')  # Erro de índice.
except Exception as erro:
    print('Ocorreu um erro inesperado.')  # Ocorreu um erro inesperado.

# Para tratar mais de um erro na mesma linha.
# A finally sempre vai ser executada normalmente com erro ou sem erro.
# A else roda se o código for executado com sucesso.

try:
    a = {}
    print(a[1])
except NameError as erro:
    print('Error', erro)
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave.')  # Erro de índice ou chave.
except Exception as erro:
    print('Ocorreu um erro inesperado.')  # Ocorreu um erro inesperado.
else:
    print('Aqui é caso o código seja executado com sucesso, ou o que você quiser')
finally:
    a = ''

print(a)

