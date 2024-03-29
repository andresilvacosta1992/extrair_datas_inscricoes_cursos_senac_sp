import requests
from bs4 import BeautifulSoup
import logging

# Configuração do logging
logging.basicConfig(filename='error.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_courses():
    try:
        # URL do site do Senac São Paulo
        url = 'https://www.sp.senac.br/'

        print(url)

        # Fazendo uma solicitação GET para a página inicial do Senac
        response = requests.get(url)

        # Verifica se a solicitação foi bem-sucedida
        if response.status_code == 200:
            # Criando um objeto BeautifulSoup para analisar o conteúdo HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            print(soup)

            # Encontrando todas as divs que contêm informações dos cursos
            course_divs = soup.find_all('div', class_='conteudo-lista')
            print(course_divs)

            # Iterando sobre as divs dos cursos para extrair informações
            for course_div in course_divs:
                # Extraindo o título do curso
                course_title = course_div.find('h2').text.strip()

                # Extraindo a descrição do curso
                course_description = course_div.find('p').text.strip()

                # Extraindo o link do curso (se disponível)
                course_link = course_div.find('a')['href'] if course_div.find('a') else 'Link não disponível'

                # Imprimindo as informações do curso
                print('Título:', course_title)
                print('Descrição:', course_description)
                print('Link:', course_link)
                print('---')

        else:
            print('Falha ao acessar o site do Senac São Paulo')

    except Exception as e:
        logging.error(f'Erro ao acessar o site do Senac São Paulo: {e}')

if __name__ == "__main__":
    get_courses()
