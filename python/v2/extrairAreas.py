from bs4 import BeautifulSoup

def extract_areas_and_save(file_path, output_path):
    # Abrir e ler o arquivo HTML
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Use Beautiful Soup para analisar o HTML
    soup = BeautifulSoup(html_content, 'lxml')

    # Encontrar a seção de áreas
    areas_link = soup.find('a', text=lambda t: t and 'Áreas' in t)
    areas_list = []
    if areas_link and areas_link.find_next_sibling('ul'):
        areas = areas_link.find_next_sibling('ul').find_all('a')
        for area in areas:
            areas_list.append(f"{area.text.strip()}: {area['href']}\n")

    # Salvar as áreas em um arquivo de texto
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(areas_list)
    print(f"Áreas salvas em: {output_path}")

if __name__ == '__main__':
    # Caminhos de entrada e saída
    file_path = 'data/menu.html'
    output_path = 'data/areas.txt'
    extract_areas_and_save(file_path, output_path)
