"""
Na associação uma classe está ligada a outra classe, porém nenhuma das duas depende da outra.
"""

from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Joãozinho')
print(escritor.nome)

caneta = Caneta('Bic')
print(caneta.marca)

maquina = MaquinaDeEscrever()
print(maquina)

print(escritor.nome)
print(caneta.marca)
maquina.escrever()

# Utilizando o método de associação com a variável None em Escritor.

escritor.ferramenta = caneta  # Máquina está escrevendo...
escritor.ferramenta.escrever()  # Caneta está escrevendo...

"""Caso coloquemos um del escritor, e após isso seja inserido um print(caneta.marca)
ou um maquina.escrever() eles iram relatar os valores normalmente, pois são independentes
como citado no início deste arquivo."""

