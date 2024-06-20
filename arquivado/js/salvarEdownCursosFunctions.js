// Função para realizar a consulta e armazenar os resultados no localStorage
function realizarConsultaEArmazenar() {
    var enderecoUnidade = document.querySelector('.ssp-ofertas__endereco-unidade').textContent.trim();
    var periodoCurso = document.querySelector('.ssp-card-oferta-curso__item-data-periodo').textContent.trim();
    var diaEHora = document.querySelector('.ssp-card-oferta-curso__dia-hora-item__dia').textContent.trim();
    var dataInscricao = document.querySelector('.ssp-container-botao-bolsa').textContent.trim();
    var cargaHoraria = document.querySelector('.ssp-card-detalhe-curso__secundary-info-carga-horaria').textContent.trim();
    
    // Capturar o título da página
    var tituloPagina = document.title;

    // Concatenar os valores capturados em uma única string separada por vírgulas
    var valoresSeparadosPorVirgula = `${tituloPagina}|||${enderecoUnidade}|||${periodoCurso}|||${diaEHora}|||${dataInscricao}|||${cargaHoraria}`;

    // Verificar se já existem resultados no localStorage
    var resultados = localStorage.getItem('resultados');

    // Se já houver resultados, adicionar os novos resultados aos existentes
    if (resultados) {
        resultados += `\n${valoresSeparadosPorVirgula}`;
    } else {
        resultados = valoresSeparadosPorVirgula;
    }

    // Armazenar os resultados atualizados no localStorage
    localStorage.setItem('resultados', resultados);
}

// Função para baixar todos os resultados armazenados como um arquivo CSV
function baixarResultadosCSV() {
    var resultados = localStorage.getItem('resultados');

    // Verificar se existem resultados no localStorage
    if (resultados) {
        // Criar um elemento de link temporário
        var link = document.createElement('a');
        link.href = 'data:text/csv;charset=utf-8,' + encodeURIComponent(resultados);
        link.download = 'resultados.csv';
        link.click();
    } else {
        console.log('Não há resultados para baixar.');
    }
}
