// Seleciona todos os elementos com a classe 'ssp-card-curso-search__tag-formato-title'
const elementos = document.querySelectorAll('.ssp-card-curso-search__tag-formato-title');

// Função para extrair informações de cada elemento
function extrairInformacoes(elemento) {
    const baseURI = elemento.baseURI; // URL base do documento onde o elemento está
    const title = elemento.innerHTML; // Título do elemento (atributo 'title')

    // Retorna um objeto com as informações
    return { baseURI, title };
}

// Array para armazenar as informações extraídas de cada elemento
const informacoesElementos = [];

// Loop para percorrer todos os elementos e extrair informações
elementos.forEach(elemento => {
    const informacoes = extrairInformacoes(elemento);
    informacoesElementos.push(informacoes);
});

// Exibe as informações extraídas no console
console.log(informacoesElementos);
