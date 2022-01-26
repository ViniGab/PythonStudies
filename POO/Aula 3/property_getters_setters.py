"""
Abaixo um motivo para utilização do getter setter, alguem incluiu o preço
do produto como R$15, ou seja, na operação gerada em desconto ocorrerá erro devido
ao formato do preço.
"""
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco *(percentual / 100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.replace('A', '@')

    # Getter
    @property  # decorador
    def preco(self):
        return self._preco  # Por convenção utilizamos o _ antes do nome para não gerar erro.

    # Setter
    @preco.setter  # O nome da propriedade que você quer .setter.
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

p1 = Produto('CAMISETA', 50)
p1.desconto(10)
print(p1.preco)  # 45.0

p2 = Produto('CANECA', 'R$15')
p2.desconto(10)
print(p2.preco)  # 13.5

print(p1.nome)  # C@MISET@
print(p2.nome)  # C@NEC@


