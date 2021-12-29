# For / Else em Python

variavel = ['Luiz Otavio', 'Joãozinho', 'Maria']

# for valor in variavel:
#     if valor.startswith('J'):
#         print(f'{valor} começa com "J"')
#     #break  #Luiz Otavio
#     #continue #Imprime todos.
#     else:
#         print(f'{valor} não começa com "J"')

comeca_com_j = False

for valor in variavel:
    if valor.lower().startswith('j'):  #verifica maiúsculas e minúsculas.
        pass
    print(valor)





