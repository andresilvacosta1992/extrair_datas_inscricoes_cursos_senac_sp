import sys
from bs4 import BeautifulSoup
import os

def extrairClass(arquivoEntrada, tagClass, arquivoSaida):
    # Garantir que o diretório onde o arquivo de saída será criado exista
    os.makedirs(os.path.dirname(arquivoSaida), exist_ok=True)

    try:
        with open(arquivoEntrada, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()

        # Parsear o conteúdo HTML com BeautifulSoup
        soup = BeautifulSoup(conteudo, 'html.parser')

        # Encontrar todos os elementos com a classe especificada
        elementos = soup.find_all(class_=tagClass)

        # Criar ou abrir o arquivo de saída
        with open(arquivoSaida, 'w', encoding='utf-8') as saida:
            # Escrever o conteúdo de cada elemento encontrado no arquivo de saída
            for elem in elementos:
                saida.write(str(elem) + '\n')  # Usar 'str(elem)' para incluir tags HTML

    except FileNotFoundError:
        print(f"Erro: O arquivo {arquivoEntrada} não foi encontrado.")
    except Exception as e:
        print(f"Erro ao processar o arquivo {arquivoEntrada}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:  # Corrigir a checagem para esperar 4 argumentos
        print("Uso: python extrairClass.py <arquivoEntrada> <tagClass> <arquivoSaida>")
    else:
        arquivoEntrada = sys.argv[1]
        tagClass = sys.argv[2]
        arquivoSaida = sys.argv[3]
        extrairClass(arquivoEntrada, tagClass, arquivoSaida)
