from bs4 import BeautifulSoup

def extract_information(file_path):
    # Abrir e ler o arquivo HTML
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Use Beautiful Soup para analisar o HTML
    soup = BeautifulSoup(html_content, 'lxml')

    # Encontrar todas as áreas, tipos e unidades com checagem de nullidade
    areas_link = soup.find('a', text=lambda t: t and 'Áreas' in t)
    if areas_link and areas_link.find_next_sibling('ul'):
        areas = areas_link.find_next_sibling('ul').find_all('a')
        print("Áreas:")
        for area in areas:
            print(f"- {area.text}: {area['href']}")

    tipos_link = soup.find('a', text=lambda t: t and 'Tipos' in t)
    if tipos_link and tipos_link.find_next_sibling('ul'):
        tipos = tipos_link.find_next_sibling('ul').find_all('a')
        print("\nTipos:")
        for tipo in tipos:
            print(f"- {tipo.text}: {tipo['href']}")

    unidades_link = soup.find('a', text=lambda t: t and 'Unidades' in t)
    if unidades_link and unidades_link.find_next_sibling('ul'):
        unidades = unidades_link.find_next_sibling('ul').find_all('a')
        print("\nUnidades:")
        for unidade in unidades:
            print(f"- {unidade.text}: {unidade['href']}")
    else:
        print("\nUnidades: Não encontradas")

if __name__ == '__main__':
    file_path = 'data/menu.html'
    extract_information(file_path)
