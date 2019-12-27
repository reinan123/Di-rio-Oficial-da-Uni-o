import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import datetime

def enviar():
    os.chdir ('\\\\fs\\Departamentos\\SNTTA\\DTROD\\CGGR\\05 - Projetos\\Robo Diario Oficial Uniao\\Dados DOU') #caminho onde o arquivo está salvo
    now = datetime.now()
    try:
        list = ['anibal.almeida@infraestrutura.gov.br', 'reinan-rp@hotmail.com', 'luciano.campos@infraestrutura.gov.br',          #lista de destinatários
                'ademir.oliveira@infraestrutura.gov.br', 'amanda.marinho@infraestrutura.gov.br', 'constantino.junior@infraestrutura.gov.br', 'roger.pegas@infraestrutura.gov.br',
                'erick.galeno@infraestrutura.gov.br', 'helen.rezende@infraestrutura.gov.br', 'herik.lopes@infraestrutura.gov.br', 'izabel.moreira@infraestrutura.gov.br',
                'jaciara.ximenes@infraestrutura.gov.br', 'jorge.conceicao@infraestrutura.gov.br', 'jose.t.oliveira@infraestrutura.gov.br', 'katia.tancon@infraestrutura.gov.br',
                'leonardo.rabelo@infraestrutura.gov.br', 'livia.fujii@infraestrutura.gov.br', 'luciano.lourenco@infraestrutura.gov.br', 'luciely.martins@infraestrutura.gov.br',
                'marcelo.gottardello@infraestrutura.gov.br', 'mariacunha.ribeiro@infraestrutura.gov.br', 'nicolli.iacobucci@infraestrutura.gov.br', 'roberto.silva@infraestrutura.gov.br']
        #list = ['reinan-rp@hotmail.com']
        destinatario = ','.join(list) #transformando a lista em string
        De = 'reinan.oliveira@infraestrutura.gov.br' #seu email

        msg = MIMEMultipart()
        msg['From'] = De #cabeçalho
        msg['To'] = destinatario #cabeçalho
        msg['Subject'] = 'Diário Oficial' #cabeçalho

        ultAtualizacao = os.path.getmtime('Diário Oficial.txt')
        dataHoraArq = datetime.fromtimestamp(ultAtualizacao).strftime('%d-%m-%Y')

        if dataHoraArq == now.strftime('%d-%m-%Y'):
            body = '\nPrezados, \nSegue em anexo o documento que contém as informações do Diário Oficial da União - Seção 3 do dia de hoje, referente aos assuntos: (Pavimentação, Construção, Adequação e Duplicação).\n Att. CGGR'  #corpo da mensagem

            msg.attach(MIMEText(body, 'plain'))
            filename = 'Diário Oficial.txt'  #nome do arquivo a ser enviado como anexo
            attachment = open('Diário Oficial.txt', 'rb')

            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment', filename='Diário Oficial.txt')

            msg.attach(part)

            attachment.close()
        else:
            body = '\nPrezados, \nNão houve publicações no dia de hoje no Diário Oficial da União - Seção 3, referente aos assuntos: (Pavimentação, Construção, Adequação e Duplicação).\n Att. CGGR'
            msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('SMTP.office365.com', 587) #servidor e porta do do seu email
        server.starttls()
        server.login(De, 'Infra2020') #seu email e senha
        text = msg.as_string() #convertendo a mensagem para string
        server.sendmail(De, list, text) #enviando o email
        server.quit() #fechando o serviço
        #print('\nEmail enviado com sucesso!')

    except Exception as e:
        pass
        #print('\nErro ao enviar o email!')
        #print(e)