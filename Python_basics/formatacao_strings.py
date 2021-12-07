nome = 'Luiz Otávio'
idade = 32
altura = 1.80
e_maior = idade > 18

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
data_1 = True
data_atual = 2019
peso = 80
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{0} tem {1} anos de idade e seu imc é {2}'.format(nome, idade, imc))