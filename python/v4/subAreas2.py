import json
from Class import extrairClass

def subAreas2():
    with open('data/areas.json', 'r', encoding='utf-8') as file:
        areas = json.load(file) 
    for area in areas:
        extrairClass(f'data/subAreas/subAreas1/{area}.html', 'nav-btn-filter', f'data/subAreas/subAreas2/{area}.html')

if __name__ == "__main__":
    subAreas2()
