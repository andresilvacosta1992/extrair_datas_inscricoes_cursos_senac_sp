document.addEventListener('DOMContentLoaded', function() {
    const captureButton = document.getElementById('captureButton');
    captureButton.addEventListener('click', captureInformation);
  });
  
  function captureInformation() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      chrome.scripting.executeScript({
        target: { tabId: tabs[0].id },
        function: captureAndStoreInformation
      });
    });
  }
  
  function captureAndStoreInformation() {
    var enderecoUnidade = document.querySelector('.ssp-ofertas__endereco-unidade').textContent.trim();
    var periodoCurso = document.querySelector('.ssp-card-oferta-curso__item-data-periodo').textContent.trim();
    var diaEHora = document.querySelector('.ssp-card-oferta-curso__dia-hora-item__dia').textContent.trim();
    var dataInscricao = document.querySelector('.ssp-container-botao-bolsa').textContent.trim();
    var valoresSeparadosPorVirgula = enderecoUnidade + '|||' + periodoCurso + '|||' + diaEHora + '|||' + dataInscricao;
    console.log(valoresSeparadosPorVirgula);
  
    // Armazenar no Local Storage
    chrome.storage.local.get('capturedInformation', function(data) {
      let capturedInformation = data.capturedInformation || [];
      capturedInformation.push(valoresSeparadosPorVirgula);
      chrome.storage.local.set({ 'capturedInformation': capturedInformation });
    });
  }
  