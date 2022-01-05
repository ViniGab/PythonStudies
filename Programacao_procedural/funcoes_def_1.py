# def funcao(msg):  #msg no caso é o parâmetro
#     print(msg)
#
# funcao()
# funcao()
# funcao()

#Damos nos nomes de Olá e usuário para os parâmetros caso os mesmos sejam chamados sem nenhum argumento.
def saudacao(msg='Olá', nome='usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    print(msg, nome)
    return f'{msg} {nome}'

saudacao('Olá', 'Vinicius')
saudacao('Olá', 'Carlos')
saudacao('Olá', 'Henrique')
saudacao('Olá', 'Tatiana')

variavel = saudacao()

print(variavel)  #Olá usuário
