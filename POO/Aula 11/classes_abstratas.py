from abc import ABC, abstractmethod
from conta_poupanca import ContaPoupanca
from conta_corrente import ContaCorrente

# Com os dois imports acima já conseguimos criar classes abstratas.


class A(ABC):
    @abstractmethod
    def falar(self):
        pass


class B(A):
    def falar(self):
        print('Falando... B...')

# a = A() - Nesse caso da erro, pois a classe A é abstrata e não pode ser instanciada
# Apesar de não poder ser instanciada podemos utiliza-la na Class B e instanciar da maneira abaixo.

a = B()
a.falar()

cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(10)
cp.sacar(5)  # Agência: 1111 Conta: 2222 Saldo: 5
cp.sacar(5)  # Agência: 1111 Conta: 2222 Saldo: 0
cp.sacar(1)  # Saldo insuficiente

print('#######################')

cc = ContaCorrente(agencia=1111, conta=3333, saldo=0, limite=100)
cc.depositar(100)
cc.depositar(100)
cc.sacar(280)  # Agência: 1111 Conta: 3333 Saldo: -80
cc.sacar(280)  # Saldo insuficiente

