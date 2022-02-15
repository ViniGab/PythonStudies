"""
Metaclasses em Python são as classes que criam outras classes;
Em Python tudo é um objeto, incluindo as classes.
Metaclasses são as "classes" que criam classes.
type é uma metaclasse(!!!???)
"""


class A:  # Essa é uma metaclasse que cria outras classes.
    attr = 'Valor'

a = A()
b = A()
c = A()

class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'B':
            return type.__new__(mcs, name, bases, namespace)

        if 'b_fala' not in namespace:
            print(f'Oi, você precisa criar o método b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um método, e não um atributo em {name}.')
        print(namespace)

        return type.__new__(mcs, name, bases, namespace)

class B(metaclass=Meta):
    def fala(self):
        self.b_fala()

class C(B):
    teste = 'Valor'
    pass
    # def b_fala(self):
    #     print('oi')
    def sei_la(self):
        pass
d = B()
