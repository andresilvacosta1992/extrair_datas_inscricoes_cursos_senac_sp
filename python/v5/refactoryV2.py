import os
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import unidecode
import shutil

def setup_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def load_json_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json_file(data, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Data saved to {filepath}")

def download_page(url, output_path):
    driver = setup_driver()
    try:
        driver.get(url)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(driver.page_source)
        print(f"Page downloaded to {output_path}")
    finally:
        driver.quit()

def extract_elements(filepath, class_name):
    with open(filepath, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
    return [unidecode.unidecode(elem.text).lower().replace(' ', '-') for elem in soup.find_all(class_=class_name)]

# Example usage
if __name__ == "__main__":
    areas = load_json_file('data/areas.json')
    for area in areas:
        html_path = f"data/html/{area}.html"
        download_page(f"https://www.sp.senac.br/areas/{area}", html_path)
        subareas = extract_elements(html_path, 'nav-btn-filter')
        save_json_file(subareas, f"data/json/{area}.json")
