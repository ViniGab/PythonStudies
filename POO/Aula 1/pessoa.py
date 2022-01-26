# O nome da classe é sempre iniciado com letra maiúscula.
# Em caso de nomes compostos digitamos as primeiras letras maiúsculas.

# Um método é uma função que pertence à classe, como segue abaixo:
# O self simboliza o próprio objeto chamado, no caso possível ver em classes.py com o p1.falar.
# Para mais de um atributo usamos o __init__ do Python.
# O parâmetro inicial é self por convenção, mas pode ser qualquer coisa.
# Não contamos o self, pois ele referencia o nome do objeto/variável, contamos a partir do nome.
from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

        # variavel = 'Valor' # Essa variável está disponível apenas nesse método/função.
        # print(variavel)  # Caso eu crie outro método e inclua a variável ocorrerá erro de escopo.
        # Porém podemos usar em outros locais as variáveis com self, como self.nome em outros métodos.

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando nada.')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True  # Precisamos chamar a variável como True, já que o parâmetro inicial foi False.

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return

        print(f'{self.nome} parou de comer')
        self.comendo = False

# Podemos também ter variáveis da classe.

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade


"""
PascalCase - significa que todas as palavras iniciam com letra maiúscula e nada é usado para separá-las,
como em: MinhaClasse, Classe, MeuObjeto, MeuProgramaMuitoLegal. Essa á a convenção utilizada para classes em Python;

camelCase - a única diferença de camelCase para PascalCase é a primeira letra. Em camelCase a primeira letra sempre será
minúscula e o restante das palavras deverá iniciar com letra maiúscula. Como em: minhaFuncao, funcaoDeSoma, etc... 
Essa conversão não é usada em Python (apesar de eu confundir as duas e às vezes acabar chamando camelCase de PascalCase
ou vice-versa, mas agora você sabe a diferença);

snake_case - este é o padrão usado em Python para definir qualquer coisa que não for uma classe. Todas as letras serão 
minúsculas e separadas por um underline, como em: minha_variavel, funcao_legal, soma.
"""