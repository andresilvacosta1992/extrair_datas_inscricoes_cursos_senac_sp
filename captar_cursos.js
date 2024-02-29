// Seleciona todos os elementos âncora com as classes desejadas
const links = document.querySelectorAll('a.text-decoration-none.ck-curso');

// String para armazenar os valores dos hrefs separados por quebra de linha
let hrefsSeparatedByNewLine = '';

// Itera sobre os elementos selecionados
links.forEach((link, index) => {
    // Recupera o valor do atributo href de cada âncora
    const href = link.getAttribute('href');
    
    // Adiciona o valor do href à string, seguido de uma quebra de linha, exceto para o último elemento
    hrefsSeparatedByNewLine += href + (index !== links.length - 1 ? '\n' : '');
});

// Imprime os valores dos hrefs no console, separados por quebra de linha
console.log(hrefsSeparatedByNewLine);
