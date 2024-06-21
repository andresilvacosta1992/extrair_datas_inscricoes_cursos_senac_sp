import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json
import unidecode
import shutil 

def setup_driver():    
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920x1080") 
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")
    chrome_options.add_argument("accept-language=en-US,en;q=0.9")
    chrome_options.add_argument("accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
    chrome_options.add_argument("referer=https://www.google.com/")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def downloadPagina(link, output_path):
    driver = setup_driver()
    try:
        driver.get(link)
        time.sleep(2) 
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(driver.page_source)
        print(f"Download concluído: {output_path}")
    except Exception as e:
        print(f"Erro ao baixar a página: {e}")
    finally:
        driver.quit()

def downPagePrincipal():
    downloadPagina("https://www.sp.senac.br/", "data/cache_html/paginaPrincipal.html")

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

def extrairMenuHtml():
    extrairClass('data/cache_html/paginaPrincipal.html', 'ssp-mega-menu__wrapper', 'data/cache_html/menu.html')

def extrairAreasJson(file_path='data/cache_html/menu.html', output_path='data/areas.json'):
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

with open('data/areas.json', 'r', encoding='utf-8') as file:
        areas = json.load(file)

def download_areas():
    for area in areas:
        downloadPagina(f"https://www.sp.senac.br/areas/{area}", f'data/cache_html/subAreas/subAreas1/{area}.html')
        print(f"Download da página '{area}' concluído")
        extrairClass(f'data/cache_html/subAreas/subAreas1/{area}.html', 'nav-btn-filter', f'data/cache_html/subAreas/subAreas2/{area}.html')
        print(f"foi extraído o html da class 'nav-btn-filter' do arquivo {area}.html")

def slugify(text):
    text = unidecode.unidecode(text).lower()
    text = text.replace(' ', '-')
    return text

def extrairSubAreasJson():
    area_subareas = {}
    for area in areas:
        input_path = f"data/subAreas/subAreas2/{area}.html"
        os.makedirs('data/subAreas/subAreas3', exist_ok=True)

        try:
            with open(input_path, 'r', encoding='utf-8') as file:
                conteudo = file.read()
            soup = BeautifulSoup(conteudo, 'html.parser')
            subareas = soup.find('nav', id='nav-sub-temas').find_all('a', attrs={"data-tema": True})
            area_subareas[area] = [slugify(subarea.text) for subarea in subareas]        
        except FileNotFoundError:
            print(f"Erro: O arquivo {input_path} não foi encontrado.")
        except Exception as e:
            print(f"Erro ao processar o arquivo {input_path}: {e}")
    output_path = 'data/subAreas/subAreas3/subareas.json'
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(area_subareas, file, ensure_ascii=False, indent=4)
    print(f"Subáreas extraídas e salvas em JSON em: {output_path}")

    # Copiar o arquivo JSON para a pasta data/
    destination_path = 'data/subareas.json'
    shutil.copy(output_path, destination_path)
    print(f"Cópia do arquivo JSON salva em: {destination_path}")


def main():
    #downPagePrincipal()
    #extrairMenuHtml()
    #extrairAreasJson()
    download_areas()
    #extrairSubAreasJson

if __name__ == "__main__":
    main()