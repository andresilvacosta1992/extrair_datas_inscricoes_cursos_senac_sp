from bs4 import BeautifulSoup
import os
import json

def extract_and_save(file_path, output_path):
    # Garantir que o diretório de saída existe
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Abrir e ler o arquivo HTML
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Usar Beautiful Soup para analisar o HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Dicionário para armazenar os slugs das unidades por categoria
    unidades_dict = {}

    # Lista de categorias para extrair
    categorias = [("Capital", "Capital"), ("Grande São Paulo e Litoral", "Grande São Paulo e Litoral"), ("Interior", "Interior")]

    for nome_cat, identificador in categorias:
        link = soup.find('a', text=lambda t: t and identificador in t)
        if link and link.find_next_sibling('ul'):
            slugs = [a['href'].split('/')[-1] for a in link.find_next_sibling('ul').find_all('a')]
            unidades_dict[nome_cat] = slugs

    # Salvar os dados no arquivo JSON
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(unidades_dict, file, ensure_ascii=False, indent=4)
    print(f"Unidades salvas com sucesso em: {output_path}")

if __name__ == '__main__':
    file_path = 'data/menu.html'
    output_path = 'data/unidades.json'
    extract_and_save(file_path, output_path)
