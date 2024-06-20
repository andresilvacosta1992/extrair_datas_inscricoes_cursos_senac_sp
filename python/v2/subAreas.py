from bs4 import BeautifulSoup

# Caminho para o arquivo HTML
file_path = 'data/subCursosBelezaEestetica.html'

# Carregar o conteúdo HTML do arquivo
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Analisar o HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Encontrar todos as subáreas dentro da seção de navegação
subareas = soup.find('nav', {'id': 'nav-sub-temas'}).find_all('a', {'data-tema': True})

# Criar uma lista para armazenar os slugs
slugs = []

for subarea in subareas:
    # Verificar se o atributo 'href' existe antes de tentar acessá-lo
    if 'href' in subarea.attrs:
        slug = subarea['href']
        slugs.append(slug)

# Salvar os slugs em um arquivo txt
with open('slugs_cursos.txt', 'w', encoding='utf-8') as file:
    for slug in slugs:
        file.write(slug + '\n')

print("Slugs salvos com sucesso no arquivo 'slugs_cursos.txt'")
