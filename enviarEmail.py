import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def enviar():

    os.chdir ('C:\\Users\\reinan.oliveira\\Documents\\Dou') #caminho onde o arquivo está salvo
    try:
        #list = ['anibal.almeida@infraestrutura.gov.br', 'reinan-rp@hotmail.com', 'luciano.campos@infraestrutura.gov.br'] #lista de destinatários
        list = ['reinan-rp@hotmail.com']
        destinatario = ','.join(list) #transformando a lista em string
        De = 'reinan.oliveira@infraestrutura.gov.br' #seu email

        msg = MIMEMultipart()
        msg['From'] = De #cabeçalho
        msg['To'] = destinatario #cabeçalho
        msg['Subject'] = 'Anexo-Dou' #cabeçalho

        body = '\nPrezados, \nSegue em anexo o documento que contém as informações do Diário Oficial do dia de hoje.\n Att. CGGR'  #corpo da mensagem

        msg.attach(MIMEText(body, 'plain'))
        filename = 'Diário Oficial.txt'  #nome do arquivo a ser enviado como anexo
        attachment = open('Diário Oficial.txt', 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename='Diário Oficial.txt')

        msg.attach(part)

        attachment.close()

        server = smtplib.SMTP('SMTP.office365.com', 587) #servidor e porta do do seu email
        server.starttls()
        server.login(De, 'Infra2020') #seu email e senha
        text = msg.as_string() #convertendo a mensagem para string
        server.sendmail(De, list, text) #enviando o email
        server.quit() #fechando o serviço
        print('\nEmail enviado com sucesso!')

    except Exception as e:
        print('\nErro ao enviar o email!')
        print(e)
