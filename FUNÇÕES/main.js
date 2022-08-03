let caderno = {
    modelo: 'tilibra',
    ano: 2021,
    estampa: 'mickey',
    valor: 35
};

let numerosImpares = [1, 3, 5, 7,9];

function listaPropriedades(obj) {
    console.log('\nPropriedades de um objeto:\n');

    for (propriedade in obj) {
        console.log(propriedade);
    }
}

function listaElementos(arr) {
    console.log('\nElementos de um array:\n');

    for (elemento of arr) {
        console.log(elemento);
    }
}

listaPropriedades(caderno);
listaElementos(numerosImpares);