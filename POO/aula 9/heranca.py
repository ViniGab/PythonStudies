# Associação - Usa
# Agregação - Tem
# Composição - É dono
# Herança - É.

from classes_para_heranca import *

c1 = Cliente('Luiz', 45)
print(c1.nome)
c1.falar()
c1.comprar()

a1 = Aluno('Maria', 54)
print(a1.nome)
a1.falar()
a1.estudar()

# Pessoa não tem estudar() nem comprar()

p1 = Pessoa('João', 43)
p1.falar()
