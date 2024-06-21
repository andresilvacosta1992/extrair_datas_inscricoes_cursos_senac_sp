import os
import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pyvirtualdisplay import Display


def setup_driver():
    
    chrome_options = Options()
    #proxy_ip_port = '66.78.34.223:5842'
    #chrome_options.add_argument(f'--proxy-server={proxy_ip_port}')
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920x1080") 
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    #chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")
    chrome_options.add_argument("accept-language=en-US,en;q=0.9")
    chrome_options.add_argument("accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
    chrome_options.add_argument("referer=https://www.google.com/")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def downloadPagina(link, arquivo, pasta):
    driver = setup_driver()
    try:
        url = link
        driver.get(url)
        countdown = 2
        for i in range(countdown, 0, -1):
            print(f"Aguardando {i} segundos...")
            time.sleep(1)  
        caminho_completo = os.path.abspath(os.path.join(os.getcwd(), 'data', pasta, f"{arquivo}.html"))
        os.makedirs(os.path.dirname(caminho_completo), exist_ok=True)
        with open(caminho_completo, "w", encoding="utf-8") as file:
            file.write(driver.page_source)
        print(f"download concluído")
    except Exception as e:
        print(f"Erro ao baixar a página: {e}")
    finally:
        driver.quit()

def downPagePrincipal():
    link = "https://www.sp.senac.br/"
    arquivo = "paginaPrincipal"
    pasta = ""
    print(f"fazendo download da página principal '{link}'")
    downloadPagina(link, arquivo, pasta)

import sys
from bs4 import BeautifulSoup
import os

def extrairClass(arquivoEntrada, tagClass, arquivoSaida):
    os.makedirs(os.path.dirname(arquivoSaida), exist_ok=True)
    try:
        with open(arquivoEntrada, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
        soup = BeautifulSoup(conteudo, 'html.parser')
        elementos = soup.find_all(class_=tagClass)
        with open(arquivoSaida, 'w', encoding='utf-8') as saida:
            for elem in elementos:
                saida.write(str(elem) + '\n') 
    except FileNotFoundError:
        print(f"Erro: O arquivo {arquivoEntrada} não foi encontrado.")
    except Exception as e:
        print(f"Erro ao processar o arquivo {arquivoEntrada}: {e}")


def menu():
    extrairClass('data/paginaPrincipal.html', 'ssp-mega-menu__wrapper', 'data/menu.html')

from bs4 import BeautifulSoup
import os
import json 

def areas(file_path='data/menu.html', output_path='data/areas.json'):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'lxml')
    areas_link = soup.find('a', text=lambda t: t and 'Áreas' in t)
    slugs_list = []
    if areas_link and areas_link.find_next_sibling('ul'):
        areas = areas_link.find_next_sibling('ul').find_all('a')
        for area in areas:
            url = area['href']
            slug = url.split('/')[-1]
            slugs_list.append(slug)
    with open(output_path, 'w', encoding='utf-8') as output_file:
        json.dump(slugs_list, output_file, indent=4) 
    print(f"Slugs salvos em: {output_path}")


def download_areas():
    with open('data/areas.json', 'r', encoding='utf-8') as file:
        areas = json.load(file)
    
    for area in areas:
        downloadPagina(f"https://www.sp.senac.br/areas/{area}", area, 'subAreas/subAreas1')
        print(f"Download da página '{area}' concluído e salvo em 'subAreas/subAreas1'")

if __name__ == "__main__":
    downPagePrincipal()
    menu()
    areas()
    download_areas()