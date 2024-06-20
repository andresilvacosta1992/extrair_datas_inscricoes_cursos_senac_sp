chrome.runtime.onInstalled.addListener(function() {
    console.log('Extensão instalada.');
  
    chrome.storage.local.set({ 'capturedInformation': [] });
  });
  
  chrome.action.onClicked.addListener(function(tab) {
    chrome.scripting.executeScript({
      target: { tabId: tab.id },
      function: exportToCSV
    });
  });
  
  function exportToCSV() {
    chrome.storage.local.get('capturedInformation', function(data) {
      let capturedInformation = data.capturedInformation || [];
  
      if (capturedInformation.length > 0) {
        let csvContent = 'data:text/csv;charset=utf-8,';
        capturedInformation.forEach(function(row) {
          csvContent += row + '\r\n';
        });
  
        let encodedUri = encodeURI(csvContent);
        let link = document.createElement('a');
        link.setAttribute('href', encodedUri);
        link.setAttribute('download', 'captured_information.csv');
        document.body.appendChild(link); // Required for Firefox
        link.click();
      }
    });
  }
  