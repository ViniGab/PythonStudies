# O nome da classe é sempre iniciado com letra maiúscula.
# Em caso de nomes compostos digitamos as primeiras letras maiúsculas.

from pessoa import Pessoa

p1 = Pessoa('Luiz', 29)
p2 = Pessoa('João', 32)

# Quando fazendo uma estância de uma classe nós estamos criando um objeto a partir da Classe.
# Ou seja, estamos utilizando um molde, para criar a "pessoa", os dois tem locais diferentes.

print(p1)  # <pessoa.Pessoa object at 0x008BE6A0>
print(p2)  # <pessoa.Pessoa object at 0x008BE6B8>

# p1.falar()  # Pessoa está falando...

#p1.comer()  # Luiz está comendo.

p1.comer('Maça')  # Luiz está comendo Maça.
p1.comer('Maça')  # Luiz já está comendo.
p1.falar('POO')  # Luiz não pode falar comendo.
p1.parar_comer()  # Luiz parou de comer
p1.parar_comer()  # Luiz não está comendo
p1.falar('POO')  # Luiz está falando sobre POO.
p1.falar('Política')  # Luiz já está falando.]
p1.parar_falar()  # Luiz parou de falar.

print(p1.ano_atual)  # 2022
print(p2.ano_atual)  # 2022

print(p1.get_ano_nascimento())  # 1993

print(p2.get_ano_nascimento())  # 1990



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
