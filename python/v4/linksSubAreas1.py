import json
import os

def linksSubAreas1():
    # Carregar as subáreas do arquivo JSON
    with open('data/subareas.json', 'r', encoding='utf-8') as file:
        subareas = json.load(file)

    # Dicionário para armazenar os links por subárea
    links_subareas = {}

    # Gerar links para cada subárea
    for area, subareas_list in subareas.items():
        links = [f"https://www.sp.senac.br/cursos-livres/{area}" for subarea in subareas_list]
        links_subareas[area] = links

    # Garantir que o diretório de destino existe
    os.makedirs('data/linksSubAreas', exist_ok=True)

    # Salvar os links em um arquivo JSON
    with open('data/linksSubAreas/linksSubAreas3.json', 'w', encoding='utf-8') as file:
        json.dump(links_subareas, file, ensure_ascii=False, indent=4)

    print("Links das subáreas foram salvos em 'data/linksSubAreas.json'")

if __name__ == "__main__":
    linksSubAreas1()
