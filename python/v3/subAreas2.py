import json
import os
from downPage import downloadPagina

def subAreas2():
    # Importar o array de áreas em data/areas.json
    with open('data/areas.json', 'r', encoding='utf-8') as file:
        areas = json.load(file)
    
    # Diretório para salvar os downloads
    save_directory = 'data/cache/areas'
    
    # Certifique-se de que o diretório para salvar os downloads existe
    os.makedirs(save_directory, exist_ok=True)
    
    # Para cada slug de área, fazer o download da página
    for area in areas:
        url = f"https://www.sp.senac.br/areas/{area}"
        file_name = area
        downloadPagina(url, file_name, save_directory)

# Execute a função se este script for o principal executado
if __name__ == "__main__":
    subAreas2()
