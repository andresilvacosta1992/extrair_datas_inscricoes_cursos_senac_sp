from bs4 import BeautifulSoup
import unidecode

# Caminho para o arquivo HTML
file_path = 'data/subCursosBelezaEestetica.html'

# Carregar o conteúdo HTML do arquivo
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Analisar o HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Encontrar todas as subáreas dentro da seção de navegação
subareas = soup.find('nav', {'id': 'nav-sub-temas'}).find_all('a', {'data-tema': True})

# Criar uma lista para armazenar os slugs das subáreas
slugs = []

for subarea in subareas:
    # Extrair o título de cada subárea e transformar em slug
    title = subarea.text.strip()
    slug = unidecode.unidecode(title).lower().replace(' ', '-')
    slugs.append(slug)

# Salvar os slugs em um arquivo txt
with open('data/subareas.txt', 'w', encoding='utf-8') as file:
    for slug in slugs:
        file.write(slug + '\n')

print("Slugs das subáreas salvos com sucesso no arquivo 'data/slugs_subareas.txt'")
