// Array de objetos para armazenar os dados das unidades
var unidadesSenacSP = [
    {
        "nome": "Lapa Tito",
        "url": "http://www.sp.senac.br/senac-lapa-tito"
    },
    {
        "nome": "Centro Universitário Senac - Santo Amaro",
        "url": "http://www.sp.senac.br/centro-universitario-senac-santo-amaro"
    },
    {
        "nome": "Aclimação",
        "url": "http://www.sp.senac.br/senac-aclimacao"
    },
    {
        "nome": "Francisco Matarazzo",
        "url": "http://www.sp.senac.br/senac-francisco-matarazzo"
    },
    {
        "nome": "Itaquera",
        "url": "http://www.sp.senac.br/senac-itaquera"
    },
    {
        "nome": "Jabaquara",
        "url": "http://www.sp.senac.br/senac-jabaquara"
    },
    {
        "nome": "Jardim Primavera",
        "url": "https://www.sp.senac.br/senac-jardim-primavera"
    },
    {
        "nome": "Lapa Faustolo",
        "url": "http://www.sp.senac.br/senac-lapa-faustolo"
    },
    {
        "nome": "Lapa Scipião",
        "url": "http://www.sp.senac.br/senac-lapa-scipiao"
    },
    {
        "nome": "Largo Treze",
        "url": "http://www.sp.senac.br/senac-largo-treze"
    },
    {
        "nome": "Penha",
        "url": "http://www.sp.senac.br/senac-penha"
    },
    {
        "nome": "Nações Unidas",
        "url": "http://www.sp.senac.br/senac-nacoes-unidas"
    },
    {
        "nome": "Santana",
        "url": "http://www.sp.senac.br/senac-santana"
    },
    {
        "nome": "São Miguel Paulista",
        "url": "http://www.sp.senac.br/senac-sao-miguel-paulista"
    },
    {
        "nome": "Tatuapé Cel. Luís Americano",
        "url": "http://www.sp.senac.br/senac-tatuape-cel-luis-americano"
    },
    {
        "nome": "Tatuapé Serra de Bragança",
        "url": "https://www.sp.senac.br/senac-tatuape-serra-de-braganca"
    },
    {
        "nome": "Tiradentes",
        "url": "http://www.sp.senac.br/senac-tiradentes"
    },
    {
        "nome": "Vila Prudente",
        "url": "http://www.sp.senac.br/senac-vila-prudente"
    },
    {
        "nome": "Bertioga",
        "url": "http://www.sp.senac.br/senac-bertioga"
    },
    {
        "nome": "Guarulhos Celestino",
        "url": "https://www.sp.senac.br/senac-guarulhos-celestino"
    },
    {
        "nome": "Guarulhos Faccini",
        "url": "http://www.sp.senac.br/senac-guarulhos"
    },
    {
        "nome": "Osasco",
        "url": "https://www.sp.senac.br/senac-osasco"
    },
    {
        "nome": "Santos",
        "url": "http://www.sp.senac.br/senac-santos"
    },
    {
        "nome": "Santo André",
        "url": "http://www.sp.senac.br/senac-santo-andre"
    },
    {
        "nome": "São Bernardo do Campo",
        "url": "http://www.sp.senac.br/senac-sao-bernardo-do-campo"
    },
    {
        "nome": "Taboão da Serra",
        "url": "http://www.sp.senac.br/senac-taboao-da-serra"
    },
    {
        "nome": "Americana",
        "url": "http://www.sp.senac.br/senac-americana"
    },
    {
        "nome": "Araçatuba",
        "url": "http://www.sp.senac.br/senac-aracatuba"
    },
    {
        "nome": "Araraquara",
        "url": "http://www.sp.senac.br/senac-araraquara"
    },
    {
        "nome": "Barretos",
        "url": "http://www.sp.senac.br/senac-barretos"
    },
    {
        "nome": "Bauru",
        "url": "http://www.sp.senac.br/senac-bauru"
    },
    {
        "nome": "Bebedouro",
        "url": "http://www.sp.senac.br/senac-bebedouro"
    },
    {
        "nome": "Botucatu",
        "url": "http://www.sp.senac.br/senac-botucatu"
    },
    {
        "nome": "Campinas",
        "url": "http://www.sp.senac.br/senac-campinas"
    },
    {
        "nome": "Catanduva",
        "url": "http://www.sp.senac.br/senac-catanduva"
    },
    {
        "nome": "Centro Universitário Senac - Águas de São Pedro",
        "url": "http://www.sp.senac.br/centro-universitario-senac-aguas-de-sao-pedro"
    },
    {
        "nome": "Centro Universitário Senac - Campos do Jordão",
        "url": "http://www.sp.senac.br/centro-universitario-senac-campos-do-jordao"
    },
    {
        "nome": "Franca",
        "url": "http://www.sp.senac.br/senac-franca"
    },
    {
        "nome": "Guaratinguetá",
        "url": "http://www.sp.senac.br/senac-guaratingueta"
    },
    {
        "nome": "Itapetininga",
        "url": "http://www.sp.senac.br/senac-itapetininga"
    },
    {
        "nome": "Itapira",
        "url": "http://www.sp.senac.br/senac-itapira"
    },
    {
        "nome": "Itu",
        "url": "http://www.sp.senac.br/senac-itu"
    },
    {
        "nome": "Jaboticabal",
        "url": "http://www.sp.senac.br/senac-jaboticabal"
    },
    {
        "nome": "Jaú",
        "url": "http://www.sp.senac.br/senac-jau"
    },
    {
        "nome": "Jundiaí",
        "url": "http://www.sp.senac.br/senac-jundiai"
    },
    {
        "nome": "Limeira",
        "url": "http://www.sp.senac.br/senac-limeira"
    },
    {
        "nome": "Marília",
        "url": "http://www.sp.senac.br/senac-marilia"
    },
    {
        "nome": "Mogi Guaçu",
        "url": "https://www.sp.senac.br/senac-mogi-guacu"
    },
    {
        "nome": "Ourinhos",
        "url": "https://www.sp.senac.br/senac-ourinhos"
    },
    {
        "nome": "Pindamonhangaba",
        "url": "http://www.sp.senac.br/senac-pindamonhangaba"
    },
    {
        "nome": "Piracicaba",
        "url": "http://www.sp.senac.br/senac-piracicaba"
    },
    {
        "nome": "Presidente Prudente",
        "url": "http://www.sp.senac.br/senac-presidente-prudente"
    },
    {
        "nome": "Registro",
        "url": "http://www.sp.senac.br/senac-registro"
    },
    {
        "nome": "Ribeirão Preto",
        "url": "http://www.sp.senac.br/senac-ribeirao-preto"
    },
    {
        "nome": "Rio Claro",
        "url": "http://www.sp.senac.br/senac-rio-claro"
    },
    {
        "nome": "Salto",
        "url": "http://www.sp.senac.br/senac-salto"
    },
    {
        "nome": "São Carlos",
        "url": "http://www.sp.senac.br/senac-sao-carlos"
    },
    {
        "nome": "São João da Boa Vista",
        "url": "http://www.sp.senac.br/senac-sao-joao-da-boa-vista"
    },
    {
        "nome": "São José do Rio Preto",
        "url": "http://www.sp.senac.br/senac-sao-jose-do-rio-preto"
    },
    {
        "nome": "São José dos Campos",
        "url": "http://www.sp.senac.br/senac-sao-jose-dos-campos"
    },
    {
        "nome": "Sorocaba",
        "url": "http://www.sp.senac.br/senac-sorocaba"
    },
    {
        "nome": "Taubaté",
        "url": "http://www.sp.senac.br/senac-taubate"
    },
    {
        "nome": "Votuporanga",
        "url": "http://www.sp.senac.br/senac-votuporanga"
    }
];

// Converter o array de objetos para uma string JSON
var jsonString = JSON.stringify(unidadesSenacSP);

// Imprimir a string JSON no console para verificar
console.log(jsonString);
