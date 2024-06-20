from bs4 import BeautifulSoup

def extract_information(file_path):
    # Abrir e ler o arquivo HTML
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Use Beautiful Soup para analisar o HTML
    soup = BeautifulSoup(html_content, 'lxml')

    # Encontrar todas as áreas, tipos e unidades
    areas = soup.find('a', text='Áreas').find_next_sibling('ul').find_all('a')
    tipos = soup.find('a', text='Tipos').find_next_sibling('ul').find_all('a')
    unidades = soup.find('a', text='Unidades').find_next_sibling('ul').find_all('a')

    # Imprimir os resultados
    print("Áreas:")
    for area in areas:
        print(f"- {area.text}: {area['href']}")

    print("\nTipos:")
    for tipo in tipos:
        print(f"- {tipo.text}: {tipo['href']}")

    print("\nUnidades:")
    for unidade in unidades:
        print(f"- {unidade.text}: {unidade['href']}")

if __name__ == '__main__':
    # Caminho do arquivo HTML
    file_path = 'data/menu.html'
    extract_information(file_path)
