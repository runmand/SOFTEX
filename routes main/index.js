const express = require('express');
const app = express()
const cors = require('cors')
const porta = 3000

let livros = []

app.use(cors())
app.use(express.urlencoded({extended: false}))
app.use(express.json())

app.get('/livro',(req, res) => {
    res.send(livros)
})

app.post('/livro', (req, res) => {
    const livro = req.body
    console.log(livro)
    livros.push(livro)
    res.send('O livro foi inserido com sucesso!')
})



app.listen(porta, () => {
    console.log("servidor escutando na porta 8080")
})