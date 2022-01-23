# Docker, deploy de modelos e Ciência dos Dados

<p align='center'>
<img src="imgs/banner.jpg" alt="drawing" width="60%"/>
</p>
<p align='center'>
<a href='https://br.freepik.com/fotos-vetores-gratis/projeto'>Projeto vetor criado por macrovector - br.freepik.com</a>
</p>

Esse repositório contém os arquivos referentes à seguinte série de postagens no Medium:

*0) Docker, deploy de modelos e Ciência dos Dados — parte 0/3:* do ciclo de vida de desenvolvimento de software ao de Engenharia de Machine Learning ([link](https://medium.com/@kattsonbastos/docker-deploy-de-modelos-e-ci%C3%AAncia-dos-dados-parte-0-3-do-ciclo-de-vida-de-desenvolvimento-de-9b40f7733002))

*1) Docker, deploy de modelos e Ciência dos Dados — parte 1/3:* Servindo nosso modelo com Python e Flask ([link](https://medium.com/@kattsonbastos/docker-deploy-de-modelos-e-ci%C3%AAncia-dos-dados-parte-1-3-servindo-nosso-modelo-com-python-e-flask-f3b0c6b32056))

*2) Docker, deploy de modelos e Ciência dos Dados — parte 2/3:* O que são containers e como ‘dockerizar’ nossa Flask API ([link](https://medium.com/@kattsonbastos/docker-deploy-de-modelos-e-ci%C3%AAncia-dos-dados-parte-2-3-o-que-s%C3%A3o-containers-e-como-2aa64666c557))

*3) Docker, deploy de modelos e Ciência dos Dados — parte 3/3:* deploy rápido e fácil do nosso container no Heroku! (ainda a produzir)

<links>

 O que cada diretório contém:
  
- part-1-building-api: repositório do código utilizado na postagem 1/3. Comporta o código da API desenvolvida com Flask. Além disso, contém a reamostragem dos dados, treinamento do algoritmo e os arquivos em pkl para os scalers e modelo treinado.
- part-2-using-docker: além dos arquivos anteriores, contém os arquivos referentes à construção da imagem Docker.
- part-3-deploy-heroku: contém alterações no código para subir a imagem para o Heroku, além de conter arquivos para página de formulário
