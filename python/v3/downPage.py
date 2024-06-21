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

        # Contagem regressiva antes de capturar a página
        countdown = 5
        for i in range(countdown, 0, -1):
            print(f"Aguardando {i} segundos...")
            time.sleep(1)  

        # Construir caminho completo para salvar o arquivo
        caminho_completo = os.path.abspath(os.path.join(os.getcwd(), 'data', pasta, f"{arquivo}.html"))
        os.makedirs(os.path.dirname(caminho_completo), exist_ok=True)

        # Salvando o HTML da página em um arquivo
        with open(caminho_completo, "w", encoding="utf-8") as file:
            file.write(driver.page_source)
        print(f"download concluído")
    except Exception as e:
        print(f"Erro ao baixar a página: {e}")
    finally:
        driver.quit()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Uso: python download_pagina.py <link> <arquivo> <pasta>")
    else:
        link = sys.argv[1]
        arquivo = sys.argv[2]
        pasta = sys.argv[3]
        downloadPagina(link, arquivo, pasta)
