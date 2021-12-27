"""
Formatando valores com modificadores - Aula 5

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - quantidade de casas decimais(float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
num_1 = 10
num_2 = 3
divisao = num_1/num_2
# print('{:.2f}'.format(divisao))  #ajuste de ponto flutuante
# Realizando a mesma situação acima, porém com f.

print(f'{divisao:.2f}')

num_1 = 1
print(f'{num_1:0>10}')  # 0000000001

num_2 = 1150
print(f'{num_2:X>20}')  # XXXXXXXXXXXXXXXX1150

num_3 = 300
print(f'{num_3:Y^13}')  # YYYYY300YYYYY

nome = 'Otávio Miranda'
nome_formatado1 = '{:@>20}'.format(nome)
print(nome_formatado1)  # @@@@@@Otávio Miranda

nome_formatado2 = '{n:0<20}'.format(n=nome)
print(nome_formatado2)  # Otávio Miranda000000

# Acessando índice

nome2 = 'Maria'
sobrenome = 'Eduarda'

nome_formatado3 = '{1:#^15}'.format(nome2, sobrenome)  #Formatando apenas sobrenome.
print(nome_formatado3)  # ####Eduarda####


