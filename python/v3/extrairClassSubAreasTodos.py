import json
import os
from Class import extrairClass

def classHeader():
    # Importar o array de áreas em data/areas.json
    with open('data/areas.json', 'r', encoding='utf-8') as file:
        areas = json.load(file)
    
    # Diretório onde as páginas estão salvas
    input_directory = 'pagesAreas'
    # Diretório para salvar os resultados da extração
    output_directory = 'pages/pagesAreas2'
    os.makedirs(output_directory, exist_ok=True)  # Cria o diretório se não existir

    # Acessar todas as páginas para extrair a classe desejada
    for area in areas:
        input_path = os.path.join(input_directory, f"{area}.html")
        if os.path.exists(input_path):
            extrairClass(area, 'ssp-page-area__lista-cursos-items', 'data/pagesAreas')
        else:
            print(f"Arquivo não encontrado: {input_path}")

if __name__ == "__main__":
    classHeader()
