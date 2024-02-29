import requests
from bs4 import BeautifulSoup

# Defina um User-Agent para se parecer mais com um navegador real
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

url = 'https://www.sp.senac.br/'

try:
    # Tente fazer uma solicitação GET usando o User-Agent definido
    response = requests.get(url, headers=headers)

    # Verifique se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Criando um objeto BeautifulSoup para analisar o conteúdo HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Agora você pode continuar o seu código aqui para extrair as informações do site
        # Por exemplo:
        # course_divs = soup.find_all('div', class_='conteudo-lista')
        # for course_div in course_divs:
        #     course_title = course_div.find('h2').text.strip()
        #     course_description = course_div.find('p').text.strip()
        #     course_link = course_div.find('a')['href'] if course_div.find('a') else 'Link não disponível'
        #     print('Título:', course_title)
        #     print('Descrição:', course_description)
        #     print('Link:', course_link)
        #     print('---')

    else:
        print('Falha ao acessar o site. Código de status:', response.status_code)

except requests.exceptions.RequestException as e:
    # Lidar com erros de solicitação, como conexão perdida, tempo limite, etc.
    print('Erro durante a solicitação:', e)
