"""
and, or, not
in e not in
"""

"""a = 2
b = 2
c = 3
a == b and b < c
a == b or b < c
not a == b and not b < c"""


# if not é muito usado em variáveis vazias.

a = ''

if not a:
    print('O campo está vazio')

nome = 'Luiz Otávio.'

if 'u' in nome:
    print("Existe a letra u no seu nome")
else:
    print("Não existe.")

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'luiz'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválidos.')
