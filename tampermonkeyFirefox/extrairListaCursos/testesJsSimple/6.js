var conteudo = document.querySelector('#cursos-por-subtema-container').innerHTML; // Use innerHTML para obter o conteúdo HTML
console.log(conteudo);
var regexLinks = /href="\/cursos-livres\/[^"]+"/g;
var links = conteudo.match(regexLinks); 
console.log(links);
