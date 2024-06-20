//não estou conseguindo criar o script pelo tampermonkey, criar o js para jogar direto no console;

// Encontrar o elemento <nav> pelo id
var navSubTemas = document.getElementById('nav-sub-temas');

// Verificar se o elemento foi encontrado
if (navSubTemas) {
    // Selecionar todos os elementos <a> dentro do <nav>
    var links = navSubTemas.querySelectorAll('a');
    console.log(links);

    // Criar uma lista para armazenar os textos dos links
    var listaLinks = [];
    console.log(listaLinks);

    // Iterar sobre os links e adicionar o textContent à lista
    links.forEach(function(link) {
        listaLinks.push(link.textContent.trim());
    });

    // Exibir a lista no console
    console.log(listaLinks);
} else {
    console.log('Elemento #nav-sub-temas não encontrado.');
}