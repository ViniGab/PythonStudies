# Apesar de estar disponível para todos os métodos/objetos, ano_atual é um atributo da classe.
# Ou seja, ano_atual é referente à classe e não à estância.
from random import randint

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod  # Decorador.
    def por_ano_nascimento(cls, nome, ano_nascimento):  #cls é convenção mas pode ser qualquer coisa.
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    # Static method. Não precisa da estância, nem da classe.

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand

p1 = Pessoa.por_ano_nascimento('luiz', 1987)
print(p1)  # <__main__.Pessoa object at 0x0021E6B8>
print(p1.nome, p1.idade)  # luiz 35
p1.get_ano_nascimento()  # 1987
print(Pessoa.gera_id())
print(p1.gera_id())

# Quando pensamos na estância, se será do objeto ou da própria estância, devemos pensar se aquela instância
# será usada pra todos os objetos, ou cada um terá o seu individual, no caso do ano podemos usar como estância da propria
# classe, pois todos os objetos estão no mesmo ano, porém caso fosse uma comida por exemplo, teria que ser uma estância
# no método como fizemos na aula anterior.


