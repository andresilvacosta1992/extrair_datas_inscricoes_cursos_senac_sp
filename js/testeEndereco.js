var enderecoUnidade = document.querySelector('.ssp-ofertas__endereco-unidade');
console.log('endereco: ' + enderecoUnidade);
// Verificar se enderecoUnidade contém "https://", se sim, atribuir null
enderecoUnidade = enderecoUnidade && enderecoUnidade.textContent.includes("https://") ? null : enderecoUnidade;
console.log('endereco: ' + enderecoUnidade);
