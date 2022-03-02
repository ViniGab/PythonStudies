from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays

# Sexta, 13 de junho de 2018

setlocale(LC_ALL, '')  # Seta a data de hoje

dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
formatacao = dt.strftime('%A, %d de %B de %Y')
print(formatacao)

# Com o from calendar e o mdays conseguimos verificar quantos dias tem cada mês do ano.

print(mes_atual, mdays[mes_atual])