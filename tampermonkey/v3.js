// ==UserScript==
// @name         Salvar Dados em JSON
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Captura dados de uma página e salva em JSON individualmente com Tampermonkey
// @author       Você
// @match        https://www.sp.senac.br/*
// @grant        GM_download
// ==/UserScript==

(function() {
    'use strict';

    // Função para lidar com a captura de dados e salvar em JSON
    function captureDataAndStore() {
        var enderecoUnidadeElement = document.querySelector('.ssp-ofertas__box-endereco-unidade a');
        var enderecoUnidade = enderecoUnidadeElement.textContent;

        var periodoCurso = document.querySelector('.ssp-card-oferta-curso__item-data-periodo').textContent;
        
        var diaEHora = document.querySelector('.ssp-card-oferta-curso__dia-hora-item__dia').textContent;

        var dataInscricao = document.querySelector('.ssp-container-botao-bolsa').textContent;

        var cargaHoraria = document.querySelector('.ssp-card-detalhe-curso__secundary-info-carga-horaria').textContent;

        var tituloPagina = document.title;

        // Criar objeto JSON com os dados capturados
        var jsonData = {
            "enderecoUnidade": enderecoUnidade,
            "periodoCurso": periodoCurso,
            "diaEHora": diaEHora,
            "dataInscricao": dataInscricao,
            "cargaHoraria": cargaHoraria,
            "tituloPagina": tituloPagina
        };

        // Converter o objeto JSON em uma string
        var jsonString = JSON.stringify(jsonData);

        // Nome do arquivo JSON
        var fileName = 'dados_' + tituloPagina + '.json';

        // Baixar o arquivo JSON
        GM_download({
            url: 'data:application/json;charset=utf-8,' + encodeURIComponent(jsonString),
            name: fileName,
            saveAs: true
        });
    }

    function testePeriodo() {
        var periodoCurso = document.querySelector('.ssp-card-oferta-curso__item-data-periodo');

        if (!periodoCurso || periodoCurso.textContent === "") {
            console.log("[false] O Período não possui conteúdo, não prosseguir com script");
        } else {
            console.log("[true] O Período possui conteúdo, prosseguir com script");
            captureDataAndStore();
        }
    }

    function checkForSpecificObject() {
        var enderecoUnidadeElement = document.querySelector('.ssp-ofertas__endereco-unidade');

        if (!enderecoUnidadeElement || enderecoUnidadeElement.textContent.trim() === "") {
            console.log("[false] O endereço não possui conteúdo, não prosseguir com script");
        } else {
            console.log("[true] O endereço possui conteúdo, prosseguir com script");
            testePeriodo();
        }
    }

    // Aguardar um atraso antes de verificar se o objeto específico está presente e capturar os dados
    setTimeout(function() {
        checkForSpecificObject();
    }, 3000); // Ajuste o valor do intervalo de tempo conforme necessário (em milissegundos)
})();
