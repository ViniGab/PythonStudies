variavel = 'valor'

def func():
    print(variavel)


#Quando destacado "outro valor" abaixo, a variável foi criada para a função abaixo: no escopo da mesma.
def func2():
    #global variavel
    variavel = 'Outro valor'
    print(variavel)  # o valor só está acessível dentro desta função
# Você "não consegue" alterar o valor de uma variável dentro uma função,
# Mas caso você queira pode utilizar global variavel como acima, não é uma prática recomendada
func()
func2()

print(variavel)

# Para alterar de uma forma mais limpa e que cause menos problemas ao corpo do código, podemos utilizar:
def func3(arg=None):
    arg = arg.replace('v', 'c')
    return arg

maneira_correta = func3(arg=variavel)
print(maneira_correta)
