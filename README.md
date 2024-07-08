# BotBet

## Projeto BotSite

Este projeto utiliza Selenium para automatizar tarefas de navegação web usando o navegador Firefox.

## Configuração

### Pré-requisitos

- Python 3.x instalado (recomenda-se usar um ambiente virtual)
- GeckoDriver para Firefox (veja instruções abaixo)

### Instalação das Dependências

1. Clone este repositório:

   ```
   git clone https://github.com/JoaoGabrielBr246/BotBet.git
   
   cd ProjetoBotSite

    Instale as dependências do Python:

    pip install -r requirements.txt

    Certifique-se de que o arquivo requirements.txt contenha o pacote selenium.

Configuração do GeckoDriver

O GeckoDriver é necessário para automatizar o Firefox com o Selenium. Siga as instruções abaixo para instalá-lo:
Linux

    Baixe o GeckoDriver adequado para o seu sistema operacional e versão do Firefox no site oficial do Selenium.

    Extraia o arquivo baixado e mova o executável geckodriver para um diretório no seu PATH:

    tar -xvzf geckodriver-vX.Y.Z-linux64.tar.gz
    chmod +x geckodriver
    sudo mv geckodriver /usr/local/bin/

    Substitua geckodriver-vX.Y.Z-linux64.tar.gz pelo nome do arquivo que você baixou.

Windows

    Baixe o GeckoDriver adequado para o seu sistema operacional e versão do Firefox no site oficial do Selenium.

    Extraia o arquivo baixado e adicione o diretório contendo o executável geckodriver.exe ao seu PATH do sistema.

macOS

    Instale o GeckoDriver usando o Homebrew:
    
    brew install geckodriver

Executando o Script

Para executar o script bot.py:

```
python bot.py
```

O script abrirá o navegador Firefox, navegará até o URL especificado, esperará 8 segundos, fechará o navegador e repetirá o processo. Encerre o script manualmente pressionando Ctrl+C.

    Certifique-se de que o Firefox esteja instalado no seu sistema operacional.
    Caso encontre problemas com o GeckoDriver, verifique a versão do Firefox instalada e use o GeckoDriver compatível.

