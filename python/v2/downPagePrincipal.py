from downPage import downloadPagina


def downPagePrincipal():
    link = "https://www.sp.senac.br/"
    arquivo = "paginaPrincipal"
    pasta = "data"
    print(f"fazendo download da página principal '{link}'")
    downloadPagina(link, arquivo, pasta)

if __name__ == "__main__":
    downPagePrincipal()
