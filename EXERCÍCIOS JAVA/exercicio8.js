let valorA =  10;
let valorB =  30;
let resultado = document.getElementById("resultado");
let botao = document.getElementById("botao");

// <--- os parâmetros aqui não eram necessários pois não estão sendo utilizados

    a = parseInt(valorA.value);
    b = parseInt(valorB.value);

    let soma = 0;
    for (let i = a; i <= b; i++){
        if (i % 2 === 1){
            soma += i;
            resultado.innerHTML = soma;
        }
    }

;


botao.addEventListener('click', () => {
  calculo();
});