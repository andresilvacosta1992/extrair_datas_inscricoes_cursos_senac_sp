var enderecoUnidadeElement = document.querySelector('.ssp-ofertas__box-endereco-unidade a');
console.log('Elemento completo do endereço: ', enderecoUnidadeElement);

var enderecoUnidade = enderecoUnidadeElement.textContent.trim();
console.log('conteudo a: ' + enderecoUnidade);


// Verificar se enderecoUnidadeElement contém "https://", se sim, atribuir null
var enderecoUnidade = enderecoUnidadeElement && enderecoUnidadeElement.href.includes("https://") ? null : enderecoUnidadeElement.textContent;
console.log('endereco: ' + enderecoUnidade);
