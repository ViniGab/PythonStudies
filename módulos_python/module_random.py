import random

# Vem sempre números aleatórios inteiros entre um ponto e outro.
import string

inteiro = random.randint(10, 20)

# Gera um número aleatório flutuante entre A e B

flutuante = random.uniform(10, 20)

# Gera um número aleatório de ponto flutuante entre 0 e 1.

flutuante2 = random.random()

# Gerar um número aleatório usando a função range()

inteirorange = random.randrange(900, 1000, 10) # Número entre 900 e 1000 pulando de 10 em 10.

# Sorteio com lista, usando o random.choice para um premiado apenas, ou choices para mais de um.

listasorteados = ['Luiz', 'Otávio', 'Maria', 'Rose', 'Jenny', 'Danilo', 'Felipe']
sorteio = random.choices(listasorteados, k=2)  # No k posso colocar a quantidade de gratificados no sorteio.
sorteio2 = random.sample(listasorteados, 2) # Com o sample ele não repete os nomes.

print(sorteio)
print(sorteio2)
print(inteiro)
print(inteirorange)
print(flutuante)
print(flutuante2)

# Embaralha a lista
random.shuffle(listasorteados)

print(listasorteados)

# Gera senha aleatória.
letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%*._ç'
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))

print(senha)






