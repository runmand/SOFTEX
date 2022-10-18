let notas = [2, 4, 5, 4, 3]

document.querySelector("#result").innerHTML = `
    <h2>A soma das notas é: ${notas.reduce((t, n) => n+t , 0)}</h2>
    <h2>A Média das notas é: ${notas.reduce((t, n) => n+t, 0)/notas.length}
    `
    