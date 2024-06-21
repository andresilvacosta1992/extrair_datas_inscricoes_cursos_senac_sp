import os
import json
from bs4 import BeautifulSoup

def extrair_subareas():
    # Carregar os nomes das áreas do arquivo JSON
    with open('data/areas.json', 'r', encoding='utf-8') as file:
        areas = json.load(file)

    # Processar cada área
    for area in areas:
        input_path = f"data/subAreas/subAreas2/{area}.html"
        output_path = f"data/subAreas/subAreas3/{area}.txt"

        # Garante que o diretório de saída existe
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        try:
            # Abrir o arquivo HTML para leitura
            with open(input_path, 'r', encoding='utf-8') as file:
                conteudo = file.read()

            # Parsear o conteúdo HTML com BeautifulSoup
            soup = BeautifulSoup(conteudo, 'html.parser')

            # Encontrar todos os elementos <a> com o atributo data-tema
            subareas = soup.find('nav', id='nav-sub-temas').find_all('a', attrs={"data-tema": True})

            # Abrir o arquivo de saída para escrita
            with open(output_path, 'w', encoding='utf-8') as file:
                # Escrever o nome de cada subárea no arquivo de saída
                for subarea in subareas:
                    file.write(subarea.text + '\n')
            print(f"Subáreas extraídas e salvas em: {output_path}")

        except FileNotFoundError:
            print(f"Erro: O arquivo {input_path} não foi encontrado.")
        except Exception as e:
            print(f"Erro ao processar o arquivo {input_path}: {e}")

if __name__ == "__main__":
    extrair_subareas()
