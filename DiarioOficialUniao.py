# este arquivo navega, faz os filtros pré-definidos através do selenium e captura o link que será utilizado na classe teste para extrair as infomações
from selenium import webdriver
from datetime import datetime
from selenium.common.exceptions import TimeoutException
import time
from bs4 import BeautifulSoup as bs
import requests
from _datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# exceção no dia 03/12 (comunicado)
class navDiarioOficial:
    def __init__(self): #esta função inicializa o navegador
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)

    def DOU(self): #esta função acessa a página inicial do DOU seção 3 do dia atual e filtra o órgão(MINFRA) e a organização subordinada (DNIT)

        try:
            self.driver.set_page_load_timeout(75)
            now = datetime.now()
            url = "http://www.in.gov.br/leiturajornal?secao=dou3&data=" + str(now.strftime("%d-%m-%Y"))  # 'http://www.in.gov.br/web/guest/inicio'    28-11-2019 / 19-11-2019  / 06-12-2019
            self.driver.get(url)
        except TimeoutException as e:
            self.driver.quit()
            print("Página de destino não responde.")
            navDiarioOficial.__init__(self)
            navDiarioOficial.DOU(self)

        time.sleep(5)

        orgao = 11  # MINFRA

        self.driver.find_element_by_xpath('//*[@id="slcOrgs"]/option[' + str(orgao) + ']').click()
        time.sleep(5)
        try:
            self.driver.find_element_by_xpath('//*[@id="slcOrgsSubs"]/option[@value="Departamento Nacional de Infraestrutura de Transportes"]').click()
        except:
            print("Não houve publicação referente ao Departamento Nacional de Infraestrutura de Transportes (DNIT)")

    def aviso(self): #esta função seleciona o tipo de Ato (Aviso) e valida se tem ou não informação
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="slcTipo"]/option[@value="Aviso"]').click()

        tipoAto = self.driver.find_element_by_xpath('//*[@id="slcTipo"]/option[@value="Aviso"]')
        tipoAto = tipoAto.is_enabled()
        if tipoAto == True:
            print()
        else:
            print("Hoje não há nenhum tipo de aviso.\n")
            self.DOU.link

    def extratoContrato(self): #esta função seleciona o tipo de Ato (Extrato de Contrato) e valida se tem ou não informação
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="slcTipo"]/option[@value="Extrato de Contrato"]').click()

        tipoAto = self.driver.find_element_by_xpath('//*[@id="slcTipo"]/option[@value="Extrato de Contrato"]')
        tipoAto = tipoAto.is_enabled()
        if tipoAto == True:
            print()
        else:
            print("Hoje não há nenhum tipo de Extrato de Contrato.\n")
            self.DOU.link

    def extratoRescisao(self): #esta função seleciona o tipo de Ato (Extrato de Rescisão) e valida se tem ou não informação
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="slcTipo"]/option[@value="Extrato de Rescisão"]').click()

        tipoAto = self.driver.find_element_by_xpath('//*[@id="slcTipo"]/option[@value="Extrato de Rescisão"]')
        tipoAto = tipoAto.is_enabled()
        if tipoAto == True:
            print()
        else:
            print("Hoje não há nenhum tipo de Extrato de Rescisão.\n")
            self.DOU.link

    def ResultadoJulgamento(self): #esta função seleciona o tipo de Ato (Resultado de Julgamento) e valida se tem ou não informação
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="slcTipo"]/option[@value="Resultado de Julgamento"]').click()

        tipoAto = self.driver.find_element_by_xpath('//*[@id="slcTipo"]/option[@value="Resultado de Julgamento"]')
        tipoAto = tipoAto.is_enabled()
        if tipoAto == True:
            print()
        else:
            print("Hoje não há nenhum tipo de Resultado de Julgamento.\n")
            self.DOU.link

    def linkAtual(self): #esta função captura o link atual de cada Ato selecionado para a captura dos seus dados(título e conteúdo)
        global link
        link = []

        qtdLinks = self.driver.find_elements_by_xpath('//*[@id="hierarchy_content"]/ul/li/a')
        for b in qtdLinks:
            links = b.get_attribute('href')
            link.append(links)

    def fecharBrowser(self): #esta função fecha o navegador ao final do processo
        time.sleep(5)
        self.driver.quit()


class infoDou:

    def tipoAviso(self): #função para extrair o conteúdo do Tipo de Ato Aviso
        os.chdir('S:\\DTROD\\CGGR\\05 - Projetos\\Robo Diario Oficial Uniao\\Dados DOU') #caminho onde o arquivo está salvo
        now = datetime.now() #pegando a data  atual
        url = [] #criando uma lista vazia

        url.append(link) # adicionando os links capturados no documento Dou.py em uma outra lista
        for url in link:   # lendo os links capturados
            page = requests.get(url) #fazendo a requisição da página através do link
            soup = bs(page.text, 'html.parser') #buscando o conteúdo html da página

            # conteinerInfo = soup.find(class_='texto-dou')
            identificacao = soup.find_all(class_='identifica') #buscando o título do conteúdo, através do nome da classe no html
            paragrafo = soup.find_all(class_='dou-paragraph') #buscando o texto do parágrafo do conteúdo, através do nome da classe no html

            titulo = identificacao[0].contents #buscando o título do conteúdo
            subTitulo = identificacao[1].contents #buscando o subtítulo do conteúdo

            processo = paragrafo[0].contents #buscando o número do processo do conteúdo
            corpoParagraph = paragrafo[1].contents #buscando o texto do parágrafo do conteúdo

            titulo = str(titulo) #convertendo a variável para string
            subTitulo = str(subTitulo) #convertendo a variável para string
            processo = str(processo) #convertendo a variável para string
            corpoParagraph = str(corpoParagraph) #convertendo a variável para string

            textoIdentificacao = titulo[2:-2] +'\n'+ subTitulo[2:-2] #eliminando letras e símbolos do início e final do conteúdo da variável
            textoParagraph = processo[2:-2] +'\n'+ corpoParagraph[2:-2] #eliminando letras e símbolos do início e final do conteúdo da variável

            textoIdentificacao = str(textoIdentificacao) #convertendo a variável para string
            textoParagraph = str(textoParagraph) #convertendo a variável para string

            '''print(textoIdentificacao)
            print(textoParagraph)
            print('----'*50)'''

            ultAtualizacao = os.path.getmtime('Diário Oficial.txt') #pegando a data da última atualização do arquivo
            dataHoraArq = datetime.fromtimestamp(ultAtualizacao).strftime('%d-%m-%Y') #formatando a data (dia-mês-ano)

            if dataHoraArq == now.strftime('%d-%m-%Y'): #condicional para saber se a data da última atualização é igual à data de hoje

                #escrever em um arquivo sem apagar seu conteúdo
                with open('Diário Oficial.txt', 'r', newline='', encoding='iso-8859-1') as saida: #abre o arquivo e o lê
                    conteudo = saida.readlines() #abre o arquivo e o lê
                    conteudo.append(textoIdentificacao + "\n" + textoParagraph+'\n') #adiciona um conteúdo

                with open('Diário Oficial.txt', 'w', newline='', encoding='iso-8859-1') as saida:
                    saida.writelines(conteudo) #abre novamente o arquivo e escreve o conteúdo criado anteriormente
            else:
                with open('Diário Oficial.txt', 'w', newline='', encoding='iso-8859-1') as saida: #sobrescreve o conteúdo
                    saida.write(textoIdentificacao + "\n" + textoParagraph + '\n') #sobrescreve o conteúdo

            nomeArquivo = str(datetime.now().strftime('%Y%m%d')) + '_DOU_Secao_3.txt' # salvar o arquivo com este nome
            nomeArquivoNaPasta = os.listdir('S:\\DTROD\\CGGR\\05 - Projetos\\Robo Diario Oficial Uniao\\Dados DOU') #listar todos os nomes de arquivos salvos nesta pasta

            if nomeArquivo in nomeArquivoNaPasta: #verificar se o nome do arquivo já existe na pasta de destino
                with open(str(datetime.now().strftime('%Y%m%d')) + '_DOU_Secao_3.txt', 'r', newline='', encoding='iso-8859-1') as saida:
                    conteudo = saida.readlines()
                    conteudo.append('\n' + textoIdentificacao + "\n\n" + textoParagraph + '\n')

                with open(str(datetime.now().strftime('%Y%m%d')) + '_DOU_Secao_3.txt', 'w', newline='', encoding='iso-8859-1') as saida:  # sobrescreve o conteúdo
                    saida.writelines(conteudo)
            else:
                with open(str(datetime.now().strftime('%Y%m%d')) + '_DOU_Secao_3.txt', 'w', newline='', encoding='iso-8859-1') as saida:  # sobrescreve o conteúdo
                    saida.write(textoIdentificacao + "\n" + textoParagraph + '\n')


    def tipoExtratoContrato(self): #função para extrair o conteúdo do Tipo de Ato Extrato de Contrato
        os.chdir('S:\\DTROD\\CGGR\\05 - Projetos\\Robo Diario Oficial Uniao\\Dados DOU') #caminho onde o arquivo está salvo
        now = datetime.now() #pegando a data  atual
        url = [] #criando uma lista vazia

        url.append(link)  #adicionando os links capturados no documento Dou.py em uma outra lista
        for url in link:  #lendo os links capturados
            page = requests.get(url) #fazendo a requisição da página através do link
            soup = bs(page.text, 'html.parser') #buscando o conteúdo html da página

            # conteinerInfo = soup.find(class_='texto-dou')
            identificacao = soup.find_all(class_='identifica') #buscando o título do conteúdo, através do nome da classe no html
            paragrafo = soup.find_all(class_='dou-paragraph') #buscando o texto do parágrafo do conteúdo, através do nome da classe no html

            try:
                titulo = identificacao #buscando o título do conteúdo
                processo = paragrafo[0].contents #buscando o número do processo do conteúdo
                tituloProcess = paragrafo[1].contents #buscando o texto do parágrafo do conteúdo
                corpoParagraph = paragrafo[2].contents #buscando o texto do parágrafo do conteúdo

                titulo = str(titulo) #convertendo a variável para string
                processo = str(processo) #convertendo a variável para string
                tituloProcess = str(tituloProcess) #convertendo a variável para string
                corpoParagraph = str(corpoParagraph) #convertendo a variável para string

                textoIdentificacao = titulo[23:-5] #eliminando letras e símbolos do início e final do conteúdo da variável
                textoParagraph = processo[2:-2] + '\n' + tituloProcess[2:-2] + '\n' + corpoParagraph[2:-2] #eliminando letras e símbolos do início e final do conteúdo da variável
            except:
                titulo = identificacao
                corpoParagraph = paragrafo[0].contents

                titulo = str(titulo)
                corpoParagraph = str(corpoParagraph)

                textoIdentificacao = titulo[23:-5]
                textoParagraph = '\n' + corpoParagraph[2:-2]

            textoIdentificacao = str(textoIdentificacao)
            textoParagraph = str(textoParagraph)

            '''print(textoIdentificacao)
            print(textoParagraph)
            print('----' * 50)'''

            ultAtualizacao = os.path.getmtime('Diário Oficial.txt') #pegando a data da última atualização do arquivo
            dataHoraArq = datetime.fromtimestamp(ultAtualizacao).strftime('%d-%m-%Y') #formatando a data (dia-mês-ano)

            if dataHoraArq == now.strftime('%d-%m-%Y'): #condicional para saber se a data da última atualização é igual à data de hoje

                # escrever em um arquivo sem apagar seu conteúdo
                with open('Diário Oficial.txt', 'r', newline='', encoding='iso-8859-1') as saida: #abre o arquivo e o lê
                    conteudo = saida.readlines() #abre o arquivo e o lê
                    conteudo.append('\n' + textoIdentificacao + "\n" + textoParagraph + '\n') #adiciona um conteúdo

                with open('Diário Oficial.txt', 'w', newline='', encoding='iso-8859-1') as saida: #abre novamente o arquivo e escreve o conteúdo criado anteriormente
                    saida.writelines(conteudo)  #abre novamente o arquivo e escreve o conteúdo criado anteriormente
            else:
                with open('Diário Oficial.txt', 'w', newline='', encoding='iso-8859-1') as saida: #sobrescreve o conteúdo
                    saida.write(textoIdentificacao + "\n" + textoParagraph + '\n') #sobrescreve o conteúdo

            nomeArquivo = str(datetime.now().strftime('%Y%m%d')) + '_DOU_Secao_3.txt'  # salvar o arquivo com este nome
            nomeArquivoNaPasta = os.listdir('S:\\DTROD\\CGGR\\05 - Projetos\\Robo Diario Oficial Uniao\\Dados DOU')  # listar todos os nomes de arquivos salvos nesta pasta

            if nomeArquivo in nomeArquivoNaPasta:  # verificar se o nome do arquivo já existe na pasta de destino
                with open(str(datetime.now().strftime('%Y%m%d')) + '_DOU_Secao_3.txt', 'r', newline='', encoding='iso-8859-1') as saida:
                    conteudo = saida.readlines()
                    conteudo.append('\n' + textoIdentificacao + "\n\n" + textoParagraph + '\n')

                with open(str(datetime.now().strftime('%Y%m%d')) + '_DOU_Secao_3.txt', 'w', newline='', encoding='iso-8859-1') as saida:  # sobrescreve o conteúdo
                    saida.writelines(conteudo)
            else:
                with open(str(datetime.now().strftime('%Y%m%d')) + '_DOU_Secao_3.txt', 'w', newline='', encoding='iso-8859-1') as saida:  # sobrescreve o conteúdo
                    saida.write(textoIdentificacao + "\n" + textoParagraph + '\n')



    def tipoExtratoRescisao(self): #função para extrair o conteúdo do Tipo de Ato Extrato de Rescisao    #03-12-2019
        os.chdir('S:\\DTROD\\CGGR\\05 - Projetos\\Robo Diario Oficial Uniao\\Dados DOU')
        global textoIdentificacao
        global textoParagraph
        now = datetime.now()
        url = []

        url.append(link)  # adicionando os links capturados no documento Dou.py em uma outra lista
        for url in link:  # lendo os links capturados
            page = requests.get(url)
            soup = bs(page.text, 'html.parser')

            # conteinerInfo = soup.find(class_='texto-dou')
            identificacao = soup.find_all(class_='identifica')
            paragrafo = soup.find_all(class_='dou-paragraph')

            titulo = identificacao
            corpoParagraph = paragrafo[0]

            titulo = str(titulo)
            corpoParagraph = str(corpoParagraph)

            textoIdentificacao = '\n'+titulo[23:-5]
            textoParagraph = corpoParagraph[25:-4]

            '''print(textoIdentificacao)
            print(textoParagraph)
            print('----' * 50)'''

            ultAtualizacao = os.path.getmtime('Diário Oficial.txt')
            dataHoraArq = datetime.fromtimestamp(ultAtualizacao).strftime('%d-%m-%Y')

            if dataHoraArq == now.strftime('%d-%m-%Y'):

                with open('Diário Oficial.txt', 'r', newline='', encoding='iso-8859-1') as saida:
                    conteudo = saida.readlines()
                    conteudo.append('\n' + textoIdentificacao + "\n\n" + textoParagraph + '\n')

                with open('Diário Oficial.txt', 'w', newline='', encoding='iso-8859-1') as saida:
                    saida.writelines(conteudo)
            else:
                with open('Diário Oficial.txt', 'w', newline='', encoding='iso-8859-1') as saida:
                    saida.write(textoIdentificacao + "\n\n" + textoParagraph)

            nomeArquivo = str(datetime.now().strftime('%Y%m%d')) + '_DOU_Secao_3.txt'  # salvar o arquivo com este nome
            nomeArquivoNaPasta = os.listdir('S:\\DTROD\\CGGR\\05 - Projetos\\Robo Diario Oficial Uniao\\Dados DOU')  # listar todos os nomes de arquivos salvos nesta pasta

            if nomeArquivo in nomeArquivoNaPasta:  # verificar se o nome do arquivo já existe na pasta de destino
                with open(str(datetime.now().strftime('%Y%m%d')) + '_DOU_Secao_3.txt', 'r', newline='', encoding='iso-8859-1') as saida:
                    conteudo = saida.readlines()
                    conteudo.append('\n' + textoIdentificacao + "\n\n" + textoParagraph + '\n')

                with open(str(datetime.now().strftime('%Y%m%d')) + '_DOU_Secao_3.txt', 'w', newline='', encoding='iso-8859-1') as saida:  # sobrescreve o conteúdo
                    saida.writelines(conteudo)
            else:
                with open(str(datetime.now().strftime('%Y%m%d')) + '_DOU_Secao_3.txt', 'w', newline='', encoding='iso-8859-1') as saida:  # sobrescreve o conteúdo
                    saida.write(textoIdentificacao + "\n" + textoParagraph + '\n')


    def tipoResultadoJulgamento(self):  #função para extrair o conteúdo do Tipo de Ato Resultado de Julgamento
        os.chdir('S:\\DTROD\\CGGR\\05 - Projetos\\Robo Diario Oficial Uniao\\Dados DOU')
        now = datetime.now()
        url = []
        tipo = 'Resultado de Julgamento'

        url.append(link)  # adicionando os links capturados no documento Dou.py em uma outra lista
        for url in link:  # lendo os links capturados
            page = requests.get(url)
            soup = bs(page.text, 'html.parser')

            # conteinerInfo = soup.find(class_='texto-dou')
            identificacao = soup.find_all(class_='identifica')
            paragrafo = soup.find_all(class_='dou-paragraph')

            try:
                titulo = identificacao[0].contents
                subtitulo = identificacao[1].contents
                corpoParagraph = paragrafo[0].contents

                titulo = str(titulo)
                subtitulo = str(subtitulo)
                corpoParagraph = str(corpoParagraph)

                textoIdentificacao = titulo[2:-2] + '\n' + subtitulo[2:-2]
                textoParagraph = corpoParagraph[2:-2]
            except:
                titulo = identificacao
                corpoParagraph = paragrafo

                titulo = str(titulo)
                corpoParagraph = str(corpoParagraph)

                textoIdentificacao = '\n' + titulo[23:-5]
                textoParagraph = '\n' + corpoParagraph[26:-5]

            '''print(textoIdentificacao)
            print(textoParagraph)
            print('----' * 50)'''

            ultAtualizacao = os.path.getmtime('Diário Oficial.txt')
            dataHoraArq = datetime.fromtimestamp(ultAtualizacao).strftime('%d-%m-%Y')

            if dataHoraArq == now.strftime('%d-%m-%Y'):

                with open('Diário Oficial.txt', 'r', newline='', encoding='iso-8859-1') as saida:
                    conteudo = saida.readlines()
                    conteudo.append('\n' + textoIdentificacao + "\n\n" + textoParagraph + '\n')

                with open('Diário Oficial.txt', 'w', newline='', encoding='iso-8859-1') as saida:
                    saida.writelines(conteudo)
            else:
                with open('Diário Oficial.txt', 'w', newline='', encoding='iso-8859-1') as saida:
                    saida.write(textoIdentificacao + "\n\n" + textoParagraph)

            nomeArquivo = str(datetime.now().strftime('%Y%m%d')) + '_DOU_Secao_3.txt'  # salvar o arquivo com este nome
            nomeArquivoNaPasta = os.listdir('S:\\DTROD\\CGGR\\05 - Projetos\\Robo Diario Oficial Uniao\\Dados DOU')  # listar todos os nomes de arquivos salvos nesta pasta

            if nomeArquivo in nomeArquivoNaPasta:  # verificar se o nome do arquivo já existe na pasta de destino
                with open(str(datetime.now().strftime('%Y%m%d')) + '_DOU_Secao_3.txt', 'r', newline='', encoding='iso-8859-1') as saida:
                    conteudo = saida.readlines()
                    conteudo.append('\n' + textoIdentificacao + "\n\n" + textoParagraph + '\n')

                with open(str(datetime.now().strftime('%Y%m%d')) + '_DOU_Secao_3.txt', 'w', newline='', encoding='iso-8859-1') as saida:  # sobrescreve o conteúdo
                    saida.writelines(conteudo)
            else:
                with open(str(datetime.now().strftime('%Y%m%d')) + '_DOU_Secao_3.txt', 'w', newline='', encoding='iso-8859-1') as saida:  # sobrescreve o conteúdo
                    saida.write(textoIdentificacao + "\n" + textoParagraph + '\n')

def enviar():

    os.chdir ('S:\\DTROD\\CGGR\\05 - Projetos\\Robo Diario Oficial Uniao\\Dados DOU') #caminho onde o arquivo está salvo
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

#este arquivo é o arquivo principal, onde é chamado todas as outras classes e executado de fato o programa
#este bloco inicia a classe navDiarioOficial do arquivo DOU.py e a função Dou(que faz a navegação até a página inicial do Minfra/Dnit) e a classe infoDou do arquivo teste.py
bott = navDiarioOficial()
extrair = infoDou()
bott.DOU()

#este bloco inicia a função aviso(que faz a filtragem para o tipo de Ato aviso) do arquivo DOU.py, a função link atual(que captura o link) e a função tipoAviso(que extai o conteúdo) do arquivo teste.py
try:
    bott.aviso()
    bott.linkAtual()
    extrair.tipoAviso()
except:
    pass

#este bloco inicia a função extratoContrato(que faz a filtragem para o tipo de Ato extrato de Contrato) do arquivo DOU.py, a função link atual(que captura o link) e a função tipoExtratoContrato(que extai o conteúdo) do arquivo teste.py
try:
    bott.extratoContrato()
    bott.linkAtual()
    extrair.tipoExtratoContrato()
except:
    pass

#este bloco inicia a função extratoRescisao(que faz a filtragem para o tipo de Ato extrato de Rescisao) do arquivo DOU.py, a função link atual(que captura o link) e a função tipoExtratoRescisao(que extai o conteúdo) do arquivo teste.py
try:
    bott.extratoRescisao()
    bott.linkAtual()
    extrair.tipoExtratoRescisao()
except:
    pass

#este bloco inicia a função ResultadoJulgamento(que faz a filtragem para o tipo de Ato Resultado de Julgamento) do arquivo DOU.py, a função link atual(que captura o link) e a função tipoResultadoJulgamento(que extai o conteúdo) do arquivo teste.py
try:
    bott.ResultadoJulgamento()
    bott.linkAtual()
    extrair.tipoResultadoJulgamento()
except:
    pass

#este bloco fecha o navegador e encerra a navegação
bott.fecharBrowser()

#este bloco chama a função enviar(que envia as informações por email) da arquivo enviarEmail.py
enviar()
