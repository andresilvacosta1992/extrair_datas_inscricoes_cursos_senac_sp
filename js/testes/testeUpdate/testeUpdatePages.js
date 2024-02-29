    // ==UserScript==
    // @name         teste de update pages
    // @namespace    http://tampermonkey.net/
    // @version      0.1
    // @description  teste de update pages
    // @author       Você
    // @match        https://www.sp.senac.br/*
    // @grant        none
    // ==/UserScript==

(function() {
    'use strict';

    // Lista de URLs das páginas que você deseja abrir e atualizar
    var urls = [
        'https://www.sp.senac.br/page1',
        'https://www.sp.senac.br/page2',
        'https://www.sp.senac.br/page3'
        // Adicione mais URLs conforme necessário
    ];

    // Índice da página atual
    var currentPageIndex = 0;
   
  
    // Função para abrir e atualizar a próxima página
    function openAndRefreshNextPage() {
        // Verifica se todas as páginas foram visitadas
        if (currentPageIndex >= urls.length) {
            console.log("Todas as páginas foram visitadas.");
            return;
        }

        // Obtém a URL da próxima página
        var nextPageUrl = urls[currentPageIndex];

        // Navega para a próxima página
        console.log("Abrindo e atualizando página: " + nextPageUrl);
        

        // Incrementa o índice da página atual para a próxima iteração
        currentPageIndex++;
        console.log('incrementando url');
        checkForSpecificObject();

        // Aguarda um breve período antes de verificar se o objeto específico está presente e capturar os dados
        setTimeout(function() {
            console.log('funcao setTime funcionando');
            checkForSpecificObject();
            console.log('checkFor ativado');
            window.location.href = nextPageUrl;
            openAndRefreshNextPage();

        }, 3000); // Ajuste o valor do intervalo de tempo conforme necessário (em milissegundos)
    }

    // Inicializa o processo de abrir e atualizar a próxima página
    
})();

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