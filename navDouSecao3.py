# este arquivo navega, faz os filtros pré-definidos através do selenium e captura o link que será utilizado na classe teste para extrair as infomações
from selenium import webdriver
from datetime import datetime
from selenium.common.exceptions import TimeoutException
import time


class navDiarioOficial:
    def __init__(self): #esta função inicializa o navegador
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)

    def DOU(self): #esta função acessa a página inicial do DOU seção 3 do dia atual e filtra o órgão(MINFRA) e a organização subordinada (DNIT)
        now = datetime.now()
        try:
            self.driver.set_page_load_timeout(75)
            url = "http://www.in.gov.br/leiturajornal?secao=dou3&data=" + str(now.strftime("%d-%m-%Y"))  # 'http://www.in.gov.br/web/guest/inicio'    28-11-2019 / 19-11-2019  / 06-12-2019
            self.driver.get(url)
        except TimeoutException as e:
            self.driver.quit()
            #print("Página de destino não responde, tentarei mais uma vez...")
            navDiarioOficial.__init__(self)
            navDiarioOficial.DOU(self)

        time.sleep(5)

        orgao = 11  # MINFRA

        self.driver.find_element_by_xpath('//*[@id="slcOrgs"]/option[' + str(orgao) + ']').click()
        time.sleep(5)
        try:
            self.driver.find_element_by_xpath('//*[@id="slcOrgsSubs"]/option[@value="Departamento Nacional de Infraestrutura de Transportes"]').click()
        except:
            pass
            #print("Não houve publicação referente ao Departamento Nacional de Infraestrutura de Transportes (DNIT)")

    def aviso(self): #esta função seleciona o tipo de Ato (Aviso) e valida se tem ou não informação
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="slcTipo"]/option[@value="Aviso"]').click()

        tipoAto = self.driver.find_element_by_xpath('//*[@id="slcTipo"]/option[@value="Aviso"]')
        tipoAto = tipoAto.is_enabled()
        if tipoAto == True:
            print()
        else:
            #print("Hoje não há nenhum tipo de aviso.\n")
            self.DOU.link

    def avisoLicenca(self): #esta função seleciona o tipo de Ato (Aviso de lincença) e valida se tem ou não informação
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="slcTipo"]/option[@value="Aviso de Licença"]').click()

        tipoAto = self.driver.find_element_by_xpath('//*[@id="slcTipo"]/option[@value="Aviso de Licença"]')
        tipoAto = tipoAto.is_enabled()
        if tipoAto == True:
            print()
        else:
            #print("Hoje não há nenhum tipo de aviso de licença.\n")
            self.DOU.link

    def extratoContrato(self): #esta função seleciona o tipo de Ato (Extrato de Contrato) e valida se tem ou não informação
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="slcTipo"]/option[@value="Extrato de Contrato"]').click()

        tipoAto = self.driver.find_element_by_xpath('//*[@id="slcTipo"]/option[@value="Extrato de Contrato"]')
        tipoAto = tipoAto.is_enabled()
        if tipoAto == True:
            print()
        else:
            #print("Hoje não há nenhum tipo de Extrato de Contrato.\n")
            self.DOU.link

    def extratoRescisao(self): #esta função seleciona o tipo de Ato (Extrato de Rescisão) e valida se tem ou não informação
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="slcTipo"]/option[@value="Extrato de Rescisão"]').click()

        tipoAto = self.driver.find_element_by_xpath('//*[@id="slcTipo"]/option[@value="Extrato de Rescisão"]')
        tipoAto = tipoAto.is_enabled()
        if tipoAto == True:
            print()
        else:
            #print("Hoje não há nenhum tipo de Extrato de Rescisão.\n")
            self.DOU.link

    def ResultadoJulgamento(self): #esta função seleciona o tipo de Ato (Resultado de Julgamento) e valida se tem ou não informação
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="slcTipo"]/option[@value="Resultado de Julgamento"]').click()

        tipoAto = self.driver.find_element_by_xpath('//*[@id="slcTipo"]/option[@value="Resultado de Julgamento"]')
        tipoAto = tipoAto.is_enabled()
        if tipoAto == True:
            print()
        else:
            #print("Hoje não há nenhum tipo de Resultado de Julgamento.\n")
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