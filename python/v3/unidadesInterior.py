from bs4 import BeautifulSoup
import os

def extract_unidades_interior_and_save(file_path, output_path):
    # Garantir que o diretório de saída existe
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Abrir e ler o arquivo HTML
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Use Beautiful Soup para analisar o HTML
    soup = BeautifulSoup(html_content, 'lxml')

    # Encontrar a seção de unidades do Interior
    unidades_interior_link = soup.find('a', text=lambda t: t and 'Interior' in t)
    slugs_list = []
    if unidades_interior_link and unidades_interior_link.find_next_sibling('ul'):
        unidades = unidades_interior_link.find_next_sibling('ul').find_all('a')
        for unidade in unidades:
            url = unidade['href']
            # Extrair o slug do URL
            slug = url.split('/')[-1]  # Pega a última parte do URL
            slugs_list.append(f"{slug}\n")

    # Salvar os slugs em um arquivo de texto
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(slugs_list)
    print(f"Slugs de unidades do Interior salvos em: {output_path}")

if __name__ == '__main__':
    # Caminhos de entrada e saída
    file_path = 'data/menu.html'
    output_path = 'data/unidades_interior.txt'
    extract_unidades_interior_and_save(file_path, output_path)
