from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

options = Options()
driver_path = '/usr/local/bin/geckodriver'
service = Service(driver_path)
driver = webdriver.Firefox(service=service, options=options)

url = 'https://luckbet777.bet/?r=elkgktar'

try:
    while True:
        driver.get(url)
        time.sleep(8)
        driver.quit()
        time.sleep(1)
        driver = webdriver.Firefox(service=service, options=options)

except KeyboardInterrupt:
    print("Bot encerrado pelo usuário.")
    driver.quit()
