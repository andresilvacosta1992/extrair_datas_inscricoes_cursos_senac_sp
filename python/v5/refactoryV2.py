import os
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import unidecode
import shutil
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    logging.info("Configurando o WebDriver.")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def load_json_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        logging.info(f"Arquivo JSON carregado com sucesso: {filepath}")
        return data
    except FileNotFoundError:
        logging.error(f"Arquivo não encontrado: {filepath}")
        return {}

def save_json_file(data, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    logging.info(f"Data saved to {filepath}")

def download_page(url, output_path):
    driver = setup_driver()
    try:
        driver.get(url)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(driver.page_source)
        logging.info(f"Page downloaded to {output_path}")
    except Exception as e:
        logging.error(f"Error downloading page {url}: {e}")
    finally:
        driver.quit()

def extract_elements(filepath, class_name):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        elements = [unidecode.unidecode(elem.text).lower().replace(' ', '-') for elem in soup.find_all(class_=class_name)]
        logging.info(f"Elements extracted from {filepath}")
        return elements
    except Exception as e:
        logging.error(f"Error processing file {filepath}: {e}")
        return []

# Example usage
if __name__ == "__main__":
    areas = load_json_file('data/areas.json')
    for area in areas:
        html_path = f"data/html/{area}.html"
        download_page(f"https://www.sp.senac.br/areas/{area}", html_path)
        subareas = extract_elements(html_path, 'nav-btn-filter')
        save_json_file(subareas, f"data/json/{area}.json")
