from bs4 import BeautifulSoup
import os
import json  # Importando a biblioteca json

def areas(file_path='data/menu.html', output_path='data/areas.json'):
    # Garantir que o diretório de saída existe
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Abrir e ler o arquivo HTML
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Usar Beautiful Soup para analisar o HTML
    soup = BeautifulSoup(html_content, 'lxml')

    # Encontrar a seção de áreas
    areas_link = soup.find('a', text=lambda t: t and 'Áreas' in t)
    slugs_list = []
    if areas_link and areas_link.find_next_sibling('ul'):
        areas = areas_link.find_next_sibling('ul').find_all('a')
        for area in areas:
            url = area['href']
            # Extrair o slug do URL
            slug = url.split('/')[-1]  # Pega a última parte do URL
            slugs_list.append(slug)

    # Salvar os slugs em um arquivo JSON formatado
    with open(output_path, 'w', encoding='utf-8') as output_file:
        json.dump(slugs_list, output_file, indent=4)  # Adicionando indentação para melhor legibilidade
    print(f"Slugs salvos em: {output_path}")

if __name__ == '__main__':
    # Caminhos de entrada e saída
    file_path = 'data/menu.html'
    output_path = 'data/areas.json'  # Alterando a extensão para .json
    areas(file_path, output_path)
