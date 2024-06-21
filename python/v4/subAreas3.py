import os
import json
from bs4 import BeautifulSoup
import unidecode

def slugify(text):
    # Transforma texto em slug: minúsculas, sem acentos, espaços por hifens
    text = unidecode.unidecode(text).lower()  # Remover acentos e converter para minúsculas
    text = text.replace(' ', '-')  # Substituir espaços por hifens
    return text

def subAreas3():
    # Carregar as áreas do arquivo JSON
    with open('data/areas.json', 'r', encoding='utf-8') as file:
        areas = json.load(file)

    # Dicionário para armazenar as subáreas por área
    area_subareas = {}

    for area in areas:
        input_path = f"data/subAreas/subAreas2/{area}.html"
        os.makedirs('data/subAreas/subAreas3', exist_ok=True)

        try:
            with open(input_path, 'r', encoding='utf-8') as file:
                conteudo = file.read()

            # Parsear o conteúdo HTML com BeautifulSoup
            soup = BeautifulSoup(conteudo, 'html.parser')

            # Encontrar todos os elementos <a> com o atributo data-tema
            subareas = soup.find('nav', id='nav-sub-temas').find_all('a', attrs={"data-tema": True})

            # Adicionar subáreas ao dicionário usando a área como chave
            area_subareas[area] = [slugify(subarea.text) for subarea in subareas]
        
        except FileNotFoundError:
            print(f"Erro: O arquivo {input_path} não foi encontrado.")
        except Exception as e:
            print(f"Erro ao processar o arquivo {input_path}: {e}")

    # Salvar o dicionário de subáreas em um arquivo JSON
    output_path = 'data/subAreas/subAreas3/subareas.json'
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(area_subareas, file, ensure_ascii=False, indent=4)
    print(f"Subáreas extraídas e salvas em JSON em: {output_path}")

if __name__ == "__main__":
    subAreas3()
