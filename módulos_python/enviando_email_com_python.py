from string import Template
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

meu_email = 'O e-mail de login'
sua_senha = 'Inserir sua senha'

with open('template.html', 'r') as html:
    template = Template(html.read())
    data1 = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Vinicius', data=data1)

print(corpo_msg)
msg = MIMEmultipart()
msg['from'] = 'Luiz Otávio Miranda'
msg['to'] = 'E-mail para o qual a msg será enviada'
msg['subject'] = 'Atenção: este é um e-mail de testes.'

with open('imagem.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login() # meu e-mail e senha = e-mail que está enviando a msg.
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')