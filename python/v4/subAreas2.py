import json
from Class import extrairClass

def classHeader():
    with open('data/areas.json', 'r', encoding='utf-8') as file:
        areas = json.load(file) 
    for area in areas:
        extrairClass(f'data/pagesAreas/{area}.html', 'ssp-page-area__lista-cursos-items', f'data/pagesAreasV2/{area}.html')

if __name__ == "__main__":
    classHeader()
