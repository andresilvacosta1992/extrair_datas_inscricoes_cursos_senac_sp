// ==UserScript==
// @name         Teste Console Log
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Imprime "teste" no console de todas as páginas
// @author       Você
// @match        https://www.sp.senac.br/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Função para lidar com a captura de dados e armazenamento no localStorage
    function captureDataAndStore() {
        var enderecoUnidade = document.querySelector('.ssp-ofertas__endereco-unidade');
        var periodoCurso = document.querySelector('.ssp-card-oferta-curso__item-data-periodo');
        var diaEHora = document.querySelector('.ssp-card-oferta-curso__dia-hora-item__dia');
        var dataInscricao = document.querySelector('.ssp-container-botao-bolsa');
        var cargaHoraria = document.querySelector('.ssp-card-detalhe-curso__secundary-info-carga-horaria');

        // Verificar e substituir por "sem informações" se a string estiver vazia
        enderecoUnidade = enderecoUnidade ? enderecoUnidade.textContent.trim() : 'sem informações';
        periodoCurso = periodoCurso ? periodoCurso.textContent.trim() : 'sem informações';
        diaEHora = diaEHora ? diaEHora.textContent.trim() : 'sem informações';
        dataInscricao = dataInscricao ? dataInscricao.textContent.trim() : 'sem informações';
        cargaHoraria = cargaHoraria ? cargaHoraria.textContent.trim() : 'sem informações';

        // Capturar o título da página
        var tituloPagina = document.title;

        // Imprimir no console
        console.log('endereco: ' + enderecoUnidade);
        console.log('periodo: ' + periodoCurso);
        console.log('dia e hora: ' + diaEHora);
        console.log('dataInscrição: ' + dataInscricao);
        console.log('cargahoraria: ' + cargaHoraria);

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
        console.log('[[salvando dados em localstorage]]');
    }

    // Aguardar um atraso antes de capturar os dados e armazenar no localStorage
    setTimeout(function() {
        // Capturar dados e armazenar no localStorage após o atraso
        captureDataAndStore();
    }, 3000); // Ajuste o valor do intervalo de tempo conforme necessário (em milissegundos)
})();
