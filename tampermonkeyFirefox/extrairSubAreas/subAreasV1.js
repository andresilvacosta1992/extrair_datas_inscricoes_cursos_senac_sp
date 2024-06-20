// ==UserScript==
// @name         Extrair Subáreas
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Extrai as subáreas do código HTML especificado
// @author       Seu Nome
// @match        https://www.sp.senac.br/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Função para extrair as subáreas do código HTML
    function extrairSubareas() {

        console.log('Encontrar o elemento que contém as subáreas');
        // Encontrar o elemento que contém as subáreas
        var navSubTemas = document.getElementById('nav-sub-temas');
        console.log(navSubTemas);
        
        console.log('Verificar se o elemento foi encontrado e contém uma lista de itens');
        // Verificar se o elemento foi encontrado e contém uma lista de itens
        if (navSubTemas) {

            console.log('foi encontrado, exibir lista:');
            // Selecionar todos os elementos <a> dentro do <nav>
            var links = navSubTemas.querySelectorAll('a');
            console.log(links);

            // Iterar sobre os links e extrair o conteúdo
            links.forEach(function(link) {
                var textoLink = link.textContent.trim();
                var dataTema = link.getAttribute('data-tema');
                console.log(textoLink + ' - ' + dataTema);
            });
        } else {
            console.log('Elemento não encontrado ou sem lista de subáreas.');
        }
    }

    // Chamar a função para extrair as subáreas
    extrairSubareas();
})();
