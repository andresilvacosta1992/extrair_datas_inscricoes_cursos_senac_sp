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
            var enderecoUnidadeElement = document.querySelector('.ssp-ofertas__box-endereco-unidade a');
            var enderecoUnidade = enderecoUnidadeElement.textContent;
            console.log('endereco: ' + enderecoUnidade);

            var periodoCurso = document.querySelector('.ssp-card-oferta-curso__item-data-periodo').textContent;
            console.log('Período: ' + periodoCurso);
        
            var diaEHora = document.querySelector('.ssp-card-oferta-curso__dia-hora-item__dia').textContent;
            console.log('dia e hora: ' + diaEHora);

            var dataInscricao = document.querySelector('.ssp-container-botao-bolsa').textContent;
            console.log('dataInscrição: ' + dataInscricao);

            var cargaHoraria = document.querySelector('.ssp-card-detalhe-curso__secundary-info-carga-horaria').textContent;
            console.log('cargahoraria: ' + cargaHoraria);

            var tituloPagina = document.title;
            console.log('título: ' + tituloPagina);


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

        function testePeriodo() {
            var periodoCurso = document.querySelector('.ssp-card-oferta-curso__item-data-periodo');


            if (!periodoCurso || periodoCurso.textContent === "") {
                console.log("[false] O Periodo não possui conteúdo, não prosseguir com script");            

            } else {
                console.log("[true] O Periodo possui conteúdo, prosseguir com script");
                captureDataAndStore()

            }

        }


        function checkForSpecificObject() {
            var enderecoUnidadeElement = document.querySelector('.ssp-ofertas__endereco-unidade');

            if (!enderecoUnidadeElement || enderecoUnidadeElement.textContent.trim() === "") {
                console.log("[false] O endereço não possui conteúdo, não prosseguir com script");
            

            } else {
                console.log("[true] O endereço possui conteúdo, prosseguir com script");
                testePeriodo()
            }
        }

        // Aguardar um atraso antes de verificar se o objeto específico está presente e capturar os dados
        setTimeout(function() {
           checkForSpecificObject()
        }, 3000); // Ajuste o valor do intervalo de tempo conforme necessário (em milissegundos)
    })();
