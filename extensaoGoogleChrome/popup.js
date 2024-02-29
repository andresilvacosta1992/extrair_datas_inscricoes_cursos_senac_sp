

// Captura o título da página
var title = document.title;

// Exibe o título no console
console.log("Título da página:", title);

// Captura o título da página ativa
chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
  var activeTab = tabs[0];
  var title = activeTab.title;
  console.log("Título da página ativa2:", title);

  // Acessa o documento da guia ativa usando o objeto activeTab
  var enderecoUnidade = activeTab.document.querySelector('.ssp-ofertas__endereco-unidade')
  console.log("Endereço da unidade:", enderecoUnidade);


});

  

let testeImpressao = document.getElementById('testeImpressao');
    testeImpressao.innerHTML = localStorage;


    // Captura o título da página ativa
chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
  var activeTab = tabs[0];
  var title = activeTab.title;
  console.log("Título da página ativa:", title);

  // Acessa o documento da guia ativa usando o objeto activeTab
  chrome.scripting.executeScript({
    target: { tabId: activeTab.id },
    function: () => {
      console.log("Esta mensagem será impressa no console da página ativa.");
    }
  });
});


