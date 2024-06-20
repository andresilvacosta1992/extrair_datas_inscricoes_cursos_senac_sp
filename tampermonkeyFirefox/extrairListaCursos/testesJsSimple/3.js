// Seleciona todos os elementos com a classe 'ssp-card-curso-search__tag-formato-title'
const elementos = document.querySelectorAll('.custom-card-curso-tema__title').innerHTML;
console.log(JSON.stringify(elementos));

// Função para extrair informações de cada elemento
function extrairInformacoes(elemento) {
    const baseURI = elemento.baseURI; // URL base do documento onde o elemento está
    const title = elemento.title; // Título do elemento (atributo 'title')

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

// Converte o array de objetos em texto JSON
const informacoesJSON = JSON.stringify(informacoesElementos);

// Exibe as informações em formato JSON no console
console.log(informacoesJSON);
