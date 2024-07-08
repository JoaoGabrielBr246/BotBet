from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Configurações do navegador Firefox
options = Options()

# Caminho para o seu GeckoDriver (se estiver no PATH, não precisa especificar)
driver_path = '/usr/local/bin/geckodriver'

# Cria uma instância do serviço GeckoDriver
service = Service(driver_path)

# Cria uma instância do navegador Firefox
driver = webdriver.Firefox(service=service, options=options)

# URL que você deseja abrir
url = 'https://luckbet777.bet/?r=elkgktar'

try:
    while True:  # Loop infinito, encerre manualmente para parar
        # Abre o URL
        driver.get(url)
        print(f"Abrindo {url}")

        # Espera por 8 segundos
        time.sleep(8)

        # Fecha o navegador
        driver.quit()
        print("Fechando o navegador")

        # Aguarda um momento antes de abrir novamente
        time.sleep(1)

        # Cria uma nova instância do navegador
        driver = webdriver.Firefox(service=service, options=options)

except KeyboardInterrupt:
    # Quando o usuário pressionar Ctrl+C para encerrar
    print("Bot encerrado pelo usuário.")
    driver.quit()
