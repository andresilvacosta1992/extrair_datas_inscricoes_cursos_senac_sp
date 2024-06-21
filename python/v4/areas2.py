#download de todos as páginas de áreas

import json
import os
from downPage import downloadPagina

def download_areas():
    # Carregar o array de slugs das áreas de um arquivo JSON
    with open('data/areas.json', 'r', encoding='utf-8') as file:
        areas = json.load(file)
    
    # Diretório para salvar os downloads das páginas
    save_directory = 'pagesAreas'
    os.makedirs(save_directory, exist_ok=True)  # Cria o diretório se ele não existir
    
    # Fazer download de cada página de área e salvar o conteúdo
    for area in areas:
        url = f"https://www.sp.senac.br/areas/{area}"
        file_name = area
        downloadPagina(url, file_name, save_directory)
        print(f"Download da página '{area}' concluído e salvo em '{save_directory}/{file_name}'")

if __name__ == "__main__":
    download_areas()
