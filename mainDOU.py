#este arquivo é o arquivo principal, onde é chamado todas as outras classes e executado de fato o programa
from DOU import navDiarioOficial
from teste import *
from enviarEmail import *

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
