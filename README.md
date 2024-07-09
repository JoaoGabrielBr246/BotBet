# README - Automação Web com Selenium

Este projeto é um exemplo simples de como automatizar a abertura de um site específico usando Selenium com Python.
### Pré-requisitos:

Certifique-se de ter o Python instalado no seu sistema. Você pode baixá-lo em python.org e seguir as instruções de instalação para o seu sistema operacional.
Instalação das Dependências
## Instale o Selenium:
Abra o terminal (ou prompt de comando no Windows) e execute o seguinte comando:
```
pip install selenium
```

## Baixe e configure o WebDriver:

### ChromeDriver (para Google Chrome):

Baixe o ChromeDriver compatível com sua versão do Google Chrome em [sites.google.com/chromedriver](https://developer.chrome.com/docs/chromedriver/downloads).
Extraia o arquivo baixado e adicione o caminho do executável ao PATH do sistema.

### Configurando no Linux:
Para adicionar o ChromeDriver ao seu PATH no Linux, você pode editar o arquivo ~/.bashrc ou ~/.profile e adicionar a seguinte linha (substituindo /caminho/para/chromedriver pelo caminho onde você extraiu o ChromeDriver):
```
export PATH="/caminho/para/chromedriver:$PATH"
```
Salve o arquivo e execute source ~/.bashrc (ou source ~/.profile) para aplicar as mudanças sem reiniciar o terminal.

### Configurando no Windows:
Adicione o diretório onde o ChromeDriver está localizado ao PATH do sistema:
Procure "Editar variáveis de ambiente" na barra de pesquisa do Windows e abra.
Na janela que se abre, clique em "Variáveis de Ambiente".
Na seção "Variáveis do Sistema", clique em "Path" e depois em "Editar".
Adicione o caminho completo para o diretório onde o ChromeDriver está localizado, por exemplo, C:\caminho\para\chromedriver, e clique em OK.

### GeckoDriver (para Mozilla Firefox):

Baixe o GeckoDriver compatível com sua versão do Firefox em [github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases).
Extraia o arquivo baixado e adicione o caminho do executável ao PATH do sistema.

### Configurando no Linux:
Para adicionar o GeckoDriver ao seu PATH no Linux, você pode seguir os mesmos passos descritos acima para o ChromeDriver, substituindo o caminho para o GeckoDriver.

### Configurando no Windows:
Siga os passos descritos acima para adicionar, como feito para o Chrome, o diretório do GeckoDriver ao PATH do sistema no Windows.

## Executando o Bot
Para executar o bot, siga as instruções adequadas para seu sistema operacional:
### No Linux
Abra o terminal e navegue até o diretório do projeto:
```
cd /caminho/para/o/diretorio/BotBet
```
Execute o script Python:
```
python bot.py
```
### No Windows

Abra o prompt de comando e navegue até o diretório do projeto:
```
cd C:\caminho\para\o\diretorio\BotBet
```
Execute o script Python:
```
python bot.py
```
## Observações

Certifique-se de que o WebDriver correto esteja instalado e configurado no seu PATH antes de executar o script.
O script abrirá o navegador (Chrome ou Firefox), visitará um site que você especificará durante a execução do programa, aguardará por 8 segundos, fechará o navegador e repetirá o processo indefinidamente até ser interrompido pelo usuário (pressionando Ctrl + C).

## Encerrando o Bot

Para encerrar o bot manualmente, pressione Ctrl + C no terminal ou prompt de comando onde o script está sendo executado.
