from bs4 import BeautifulSoup

# HTML input
html_content = '''
<nav class="nav-btn-filter" id="nav-sub-temas">
<ul><li><a class="todos nav-btn-active">Todos</a></li><li><a data-tema="40609">Cabelo e Barbearia</a></li><li><a data-tema="40607">Depilação</a></li><li><a data-tema="40456">Estética</a></li><li><a data-tema="40482">Maquiagem</a></li><li><a data-tema="40611">Massoterapia e Terapias Complementares</a></li><li><a data-tema="40613">Pés e Mãos</a></li></ul>
</nav>
'''

# Parsear o conteúdo HTML
soup = BeautifulSoup(html_content, 'lxml')

# Encontrar o elemento nav pelo seu ID
nav = soup.find('nav', id='nav-sub-temas')

# Encontrar todos os links <a> com o atributo data-tema
subareas = nav.find_all('a', attrs={"data-tema": True})

# Extrair e imprimir os nomes das subáreas
for subarea in subareas:
    print(subarea.text)
