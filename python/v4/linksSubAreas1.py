def linksSubAreas1():
    # Carregar as subareas do arquivo JSON
    with open('data/subareas.json', 'r', encoding='utf-8') as file:
        subareas = json.load(file)