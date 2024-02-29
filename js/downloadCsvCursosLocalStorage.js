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