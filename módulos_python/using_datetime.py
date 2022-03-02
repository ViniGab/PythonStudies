
from datetime import datetime, timedelta

data = datetime(2019, 4, 20, 10, 53,  20)

print(data)  # 2019-04-20 10:53:20
print(data.strftime('%d/%m/%Y %H:%M:%S'))  # 20/04/2019 10:53:20

# Para fazer com que o Python transforme a string recebida em DATETIME.

data1 = datetime.strptime('20/04/2019', '%d/%m/%Y')
print(data1.timestamp())  # 1555729200.0
data2 = datetime.fromtimestamp(1555729200.0)
print(data2)  # 2019-04-20 00:00:00

#Operações com datetime

d3 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
d4 = datetime.strptime('25/04/1987 20:33:00', '%d/%m/%Y %H:%M:%S')

# Subtrair, diferença entre as datas.

dif = d4 - d3
print(dif)  # 5 days, 0:33:

