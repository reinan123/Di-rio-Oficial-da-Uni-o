# Di-rio-Oficial-da-Uni-o
Script em Python para coletar informações da seção 3 do Diário Oficial da União

O arquivo DOU.py é a classe onde se faz a navegação, usando o selenium, até a página desejada fazendo os filtros pré-definidos. E também é
extraído o link onde da acesso à publicação.

O arquivo extrairInformacao.py é a classe onde se recebe o link da publicação, extrai essa informação através do BeautifulSoup e grava em 
um arquivo txt.

O arquivo enviarEmail.py é a classe que faz o envio do arquivo por email.

O mainDOU.py é a classe principal onde é feito todas as chamadas e incialização das demais classes.

O arquivo DiarioOficialUniao.py reúne todas as classes anteriores em um único arquivo.
