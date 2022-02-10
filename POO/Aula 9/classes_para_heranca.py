# Para não repertimos o construtor nos dois abaixo usamos esse método.
# Aluno e Cliente são pessoas, então pegamos o construtor de Pessoa.
# A aula sobre a sobreposição de membros é basicamente para usarmos métodos nas subclasses com cuidado, para não sobrepor
# os anteriores.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__  # Para saber qual o cliente/aluno está falando.

    def falar(self):
        print(f'{self.nomeclasse} Falando...')

# As classes abaixo são subclasses de Pessoa, podemos também ter coisas específicas em cada uma delas.


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')

# Caso coloquemos o def falar em Cliente o ClienteVIP com o super.falar puxará
# o "Estou em CLIENTE." ao invés da class Pessoa, pois a super puxa a classe principal da cadeia anterior.

    # def falar(self):
    #     print('Estou em CLIENTE.')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} estudando...')


class ClienteVIP(Cliente):
    # Usando o construtor sem sobrepor o de Pessoa.
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        super().falar()  # Para executar primeiro o método de Pessoa falar, evitando o comentário abaixo.
        print('Outra coisa qualquer.')  # Sobrepoe o falar da classe Pessoa.
