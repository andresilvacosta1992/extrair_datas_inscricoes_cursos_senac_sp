import json
import os

def load_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Erro: Arquivo não encontrado - {filepath}")
    except json.JSONDecodeError:
        raise json.JSONDecodeError(f"Erro: Falha ao decodificar JSON - {filepath}")

def save_json(data, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    print(f"Dados salvos com sucesso em: {filepath}")

    
def linksUnidades():
    input_path = 'data/unidades.json'  # Caminho para o arquivo de entrada
    output_path = 'data/links/linksUnidades.json'  # Caminho para o arquivo de saída com uma lista simples
    base_url = "https://www.sp.senac.br/"  # URL base para os links
    os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Garantir que o diretório de saída existe
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            unidades_dict = json.load(file)
        all_links = []  # Lista para armazenar todos os links
        # Gerar links para cada unidade em cada categoria
        for unidades in unidades_dict.values():
            for unidade in unidades:
                all_links.append(base_url + unidade)  # Construir link completo e adicionar à lista
        # Salvar os links em um arquivo JSON
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(all_links, file, indent=4)  # Salva todos os links no arquivo
        print(f"Todos os links das unidades foram salvos com sucesso em: {output_path}")
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado - {input_path}")
    except json.JSONDecodeError:
        print(f"Erro: Falha ao decodificar JSON - {input_path}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def linksAreasPrincipais():
    input_path = 'data/areas.json'
    output_path = 'data/links/linksAreas.json'
    base_url = "https://www.sp.senac.br/areas/"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            areas = json.load(file)        
        links = [base_url + area for area in areas] # Criação de links para cada área        
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(links, file, indent=4)  # Salva os links no arquivo JSON        
        print(f"Links das áreas principais foram salvos com sucesso em: {output_path}")    
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado - {input_path}")
    except json.JSONDecodeError:
        print(f"Erro: Falha ao decodificar JSON - {input_path}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def linksSubAreas():
    input_path = 'data/subareas.json' 
    output_path = 'data/links/linksSubAreas.json'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            categories = json.load(file)
        all_links = []
        for category, subcategories in categories.items():
            for subcategory in subcategories:
                link = f"https://www.sp.senac.br/areas/{category}/{subcategory}"
                all_links.append(link) 
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(all_links, file, indent=4) 
        print(f"Todos os links das subcategorias foram salvos com sucesso em: {output_path}")
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado - {input_path}")
    except json.JSONDecodeError:
        print(f"Erro: Falha ao decodificar JSON - {input_path}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def main():
     linksUnidades()
     linksAreasPrincipais()
     linksSubAreas()
if __name__ == "__main__":
    main()
