# Podemos passar uma função para uma variável.

def fala_oi():
    print('Oi')

variavel = fala_oi

variavel()
print(type(variavel))  # <class 'function'>

# Criando uma função master, e dentro da função criar uma função escrava para fazer qualquer coisa.

def master(funcao):
    def slave():
        print('Agora estou decorada.')
        funcao()
    return slave

def fale_oi():
    print('Hi')

fale_oi = master(fale_oi)
fale_oi()
variavel()
print(type(variavel))  # <class 'function'>

