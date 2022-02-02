class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    # Exemplo abaixo do append utilizando outra classe, mais explicações no composicao.py

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    # Abaixo já estamos utilizando a outra classe citada acima.

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f'{self.nome} FOI APAGADO')

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}/{self.estado} FOI APAGADO')