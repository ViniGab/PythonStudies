"""
Encapsulamento é uma parte da orientação a objetos que serve para esconder
certas partes do seu código, para proteger sua aplicação/atributo/método.
"""

"""
Em outras linguagens temos os métodos public, que podem ser acessados dentro e fora
da classe, protected são os atributos que podem ser utilizados apenas na classe, ou 
nas filhas daquela classe, e private é quando o atributo só pode ser acessado dentro da classe.
"""

# O self com um underline é privado até você digitar. no caso o protected
# O privado "fortemente" é com dois underlines.

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')
bd.apaga_cliente(2)
bd.lista_clientes()

# Para acessar o atributo real quando está com dois underline.
print(bd._BaseDeDados__dados)# {'clientes': {1: 'Otávio', 3: 'Rose'}}

