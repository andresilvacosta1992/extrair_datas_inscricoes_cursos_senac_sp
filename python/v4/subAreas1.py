import json
from downPage import downloadPagina

def download_areas():
    # Carregar o array de slugs das áreas de um arquivo JSON
    with open('data/areas.json', 'r', encoding='utf-8') as file:
        areas = json.load(file)
    
    for area in areas:
        url = f"https://www.sp.senac.br/areas/{area}"
        file_name = area
        downloadPagina(url, file_name, 'subAreas/subAreas1')
        print(f"Download da página '{area}' concluído e salvo em 'subAreas/subAreas1'")

if __name__ == "__main__":
    download_areas()
