# Control + espaço após digitar para ver as opções.
from string import Template

from datetime import datetime

with open('template.html', 'r') as html:
    template = Template(html.read())
    data1 = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Vinicius', data=data1)

print(corpo_msg)