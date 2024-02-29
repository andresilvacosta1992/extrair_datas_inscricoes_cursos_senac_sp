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
    console.log('salvando dados em localstorage: ' + valoresSeparadosPorVirgula);
})();
