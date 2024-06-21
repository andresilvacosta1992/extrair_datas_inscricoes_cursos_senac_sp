import json
from downPage import downloadPagina

def download_areas():
    with open('data/areas.json', 'r', encoding='utf-8') as file:
        areas = json.load(file)
    
    for area in areas:
        downloadPagina(f"https://www.sp.senac.br/areas/{area}", area, 'subAreas/subAreas1')
        print(f"Download da página '{area}' concluído e salvo em 'subAreas/subAreas1'")

if __name__ == "__main__":
    download_areas()
