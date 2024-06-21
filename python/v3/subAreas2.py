import json
import requests
from bs4 import BeautifulSoup
import unidecode

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
    
    # Para cada slug de área, acessar a URL e extrair subáreas
    for area in areas:
        url = f"https://www.sp.senac.br/areas/{area}"
        
        # Fazer a requisição para a URL
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
            # Extrair subáreas
            slugs = extract_subareas(html_content)
            # Imprimir os slugs para cada área
            print(f"Slugs das subáreas para '{area}': {slugs}")
        else:
            print(f"Erro ao acessar {url}: Status {response.status_code}")

if __name__ == "__main__":
    subAreas2()
