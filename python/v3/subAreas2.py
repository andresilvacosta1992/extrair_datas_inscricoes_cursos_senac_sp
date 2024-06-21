import json
import os
from bs4 import BeautifulSoup
import unidecode
from downPage import downloadPagina

def extract_subareas(html_content):
    # Analisar o HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    # Encontrar todas as subáreas dentro da seção de navegação
    subareas = soup.find('nav', {'id': 'nav-sub-temas'}).find_all('a', {'data-tema': True})
    # Criar uma lista para armazenar os slugs das subáreas
    slugs = []
    for subarea in subareas:
        # Extrair o título de cada subárea e transformar em slug
        title = subarea.text.strip()
        slug = unidecode.unidecode(title).lower().replace(' ', '-')
        slugs.append(slug)
    return slugs

def subAreas2():
    # Importar o array de áreas em data/areas.json
    with open('data/areas.json', 'r', encoding='utf-8') as file:
        areas = json.load(file)
    
    # Diretório para salvar os downloads
    save_directory = 'cache/areas'
    # Certifique-se de que o diretório para salvar os downloads existe
    os.makedirs(save_directory, exist_ok=True)
    
    # Para cada slug de área, fazer o download da página e extrair subáreas
    for area in areas:
        url = f"https://www.sp.senac.br/areas/{area}"
        file_name = {area}
        output_path = os.path.join(save_directory, file_name)
        downloadPagina(url, file_name, save_directory)
        
        # Carregar o conteúdo HTML do arquivo baixado
        with open(output_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Extrair subáreas
        slugs = extract_subareas(html_content)
        
        # Salvar os slugs em um arquivo txt para cada área
        slug_save_path = os.path.join(save_directory, f"{area}_subareas.txt")
        with open(slug_save_path, 'w', encoding='utf-8') as file:
            for slug in slugs:
                file.write(slug + '\n')
        print(f"Slugs das subáreas salvos com sucesso no arquivo '{slug_save_path}'")

if __name__ == "__main__":
    subAreas2()
