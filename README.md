# Di-rio-Oficial-da-Uni-o
Script em Python para coletar informações da seção 3 do Diário Oficial da União

O arquivo "navDouSecao3.py" é a classe onde se faz a navegação, usando o selenium, até a página desejada fazendo os filtros pré-definidos. E também é extraído o link onde da acesso à publicação.

O arquivo "InformacaoDouSecao3.py" é a classe onde se recebe o link da publicação, extrai essa informação através do BeautifulSoup e grava em um arquivo txt.

O arquivo "emailClass.py" é a classe que faz o envio do arquivo por email.

O "mainDouSecao3.py" é a classe principal onde é feito todas as chamadas e incialização das demais classes.
