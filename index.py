from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import requests
from bs4 import BeautifulSoup

servico = Service(ChromeDriverManager().install())


navegador = webdriver.Chrome(service=servico)

navegador.get('http://127.0.0.1:5500/isearchfrom.com/index.html')


navegador.find_element('xpath', '//*[@id="countrytags"]').send_keys('Brasil')
time.sleep(1)
navegador.find_element('xpath', '//*[@id="deviceselect"]').click()
time.sleep(1)
navegador.find_element('xpath', '//*[@id="deviceselect"]').send_keys('w')
time.sleep(1)

navegador.find_element('xpath', '//*[@id="searchinput"]').send_keys('Kikina')
navegador.find_element('xpath', '//*[@id="city"]').send_keys('São Paulo')
time.sleep(1)

navegador.find_element('xpath', '//*[@id="searchbutton"]').click()


# Espera um tempo para que a página carregue completamente
time.sleep(5)

link = ''
requisicao = requests.get(link)
print(requisicao.text)
site= BeautifulSoup(requisicao, 'html.parser')
print()


# Fechar o navegador
navegador.quit()