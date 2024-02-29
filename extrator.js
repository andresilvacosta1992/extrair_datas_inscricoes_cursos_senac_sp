var enderecoUnidade = document.querySelector('.ssp-ofertas__endereco-unidade').textContent.trim();
var periodoCurso = document.querySelector('.ssp-card-oferta-curso__item-data-periodo').textContent.trim();
var diaEHora = document.querySelector('.ssp-card-oferta-curso__dia-hora-item__dia').textContent.trim();
var dataInscricao = document.querySelector('.ssp-container-botao-bolsa').textContent.trim();
// Concatene os valores capturados em uma única string separada por vírgulas
var valoresSeparadosPorVirgula = enderecoUnidade + '|||' + periodoCurso + '|||' + diaEHora + '|||' + dataInscricao;
// Imprima a string no console
console.log(valoresSeparadosPorVirgula);

