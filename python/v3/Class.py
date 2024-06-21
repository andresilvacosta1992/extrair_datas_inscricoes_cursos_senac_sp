import sys
from bs4 import BeautifulSoup
import os

def extrairClass(arquivoEntrada, tagClass, arquivoSaida):
    caminho = "data"  # Define o caminho base para os arquivos

    # Construir os caminhos completos para os arquivos de entrada e saída
    caminhoEntrada = os.path.join(f"{arquivoEntrada}")
    caminhoSaida = os.path.join(f"{arquivoSaida}")

    try:
        # Abrir o arquivo HTML para leitura
        with open(caminhoEntrada, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()

        # Parsear o conteúdo HTML com BeautifulSoup
        soup = BeautifulSoup(conteudo, 'html.parser')

        # Encontrar todos os elementos com a classe especificada
        elementos = soup.find_all(class_=tagClass)

        # Criar ou abrir o arquivo de saída
        with open(caminhoSaida, 'w', encoding='utf-8') as saida:
            # Escrever o conteúdo de cada elemento encontrado no arquivo de saída
            for elem in elementos:
                saida.write(str(elem) + '\n')  # Usar 'str(elem)' para incluir tags HTML

    except FileNotFoundError:
        print(f"Erro: O arquivo {caminhoEntrada} não foi encontrado.")
    except Exception as e:
        print(f"Erro ao processar o arquivo {caminhoEntrada}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:  # Corrigir a checagem para esperar 4 argumentos
        print("Uso: python extrairClass.py <arquivoEntrada> <tagClass> <arquivoSaida>")
    else:
        arquivoEntrada = sys.argv[1]
        tagClass = sys.argv[2]
        arquivoSaida = sys.argv[3]
        extrairClass(arquivoEntrada, tagClass, arquivoSaida)
