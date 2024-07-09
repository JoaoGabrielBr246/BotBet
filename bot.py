from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import shutil

def get_webdriver():
    chrome_driver_path = shutil.which('chromedriver')
    firefox_driver_path = shutil.which('geckodriver')

    try:
        if chrome_driver_path:
            options = ChromeOptions()
            service = ChromeService(chrome_driver_path)
            return webdriver.Chrome(service=service, options=options)
        elif firefox_driver_path:
            options = FirefoxOptions()
            service = FirefoxService(firefox_driver_path)
            return webdriver.Firefox(service=service, options=options)
        else:
            raise Exception("Nenhum WebDriver adequado encontrado. Certifique-se de que o ChromeDriver ou o GeckoDriver estejam instalados e no PATH.")
    except Exception as e:
        print(f"Erro ao iniciar o ChromeDriver: {e}")
        if firefox_driver_path:
            options = FirefoxOptions()
            service = FirefoxService(firefox_driver_path)
            return webdriver.Firefox(service=service, options=options)
        else:
            raise Exception("Nenhum WebDriver adequado encontrado. Certifique-se de que o GeckoDriver esteja instalado e no PATH.")

url = str(input("Digite o site que deseja visitar: "))

n = 0

try:
    while True:
        driver = get_webdriver()
        driver.get(url)
        time.sleep(8)
        driver.quit()
        n += 1
        time.sleep(1)

except KeyboardInterrupt:
    print("Bot encerrado pelo usuário.")
    print(f"Foi feito {n} acessos ao site {url}")
    driver.quit()
except Exception as e:
    print(f"Erro: {e}")
