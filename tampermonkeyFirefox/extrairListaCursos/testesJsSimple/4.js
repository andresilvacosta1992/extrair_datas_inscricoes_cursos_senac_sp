// Seleciona o elemento com a classe 'ssp-container__cursos-sem-slick'
var containerElemento = document.querySelector('#cursos-por-subtema-container');
console.log(containerElemento);


const htmlData = containerElemento;

// Expressões regulares para extrair links e títulos
const linkPattern = /<a class="text-decoration-none ck-curso" href="(.*?)" data-ck=".*?">.*?<\/a>/g;
const titlePattern = /<h6 class="ssp-card-curso__title custom-card-curso-tema__title">(.*?)<\/h6>/g;

// Função para extrair dados do HTML usando expressões regulares
function extractData(html) {
  const links = Array.from(html.matchAll(linkPattern), match => match[1]);
  const titles = Array.from(html.matchAll(titlePattern), match => match[1]);

  const courses = links.map((link, index) => ({ link, title: titles[index] }));
  return courses;
}

// Extrair dados e converter para JSON
const coursesData = extractData(htmlData);
const coursesJson = JSON.stringify(coursesData, null, 2);
console.log(coursesJson);
