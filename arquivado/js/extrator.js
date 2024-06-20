var enderecoUnidade = document.querySelector('.ssp-ofertas__endereco-unidade').textContent.trim();
var periodoCurso = document.querySelector('.ssp-card-oferta-curso__item-data-periodo').textContent.trim();
var diaEHora = document.querySelector('.ssp-card-oferta-curso__dia-hora-item__dia').textContent.trim();
var dataInscricao = document.querySelector('.ssp-container-botao-bolsa').textContent.trim();
var cargaHoraria = document.querySelector('.ssp-card-detalhe-curso__secundary-info-carga-horaria').textContent.trim();

// Capturar o título da página
var tituloPagina = document.title;

// Concatenar os valores capturados em uma única string separada por vírgulas
var valoresSeparadosPorVirgula = tituloPagina + '|||' + enderecoUnidade + '|||' + periodoCurso + '|||' + diaEHora + '|||' + dataInscricao + '|||' + cargaHoraria;

// Imprimir a string no console
console.log(valoresSeparadosPorVirgula);
