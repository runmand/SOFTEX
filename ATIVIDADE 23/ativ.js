class Aluno {
    constructor(nome, curso, semestre) {
        this.nome = nome,
            this.curso = curso,
            this.semestre = semestre
    }
    get nomeAluno() {
        return this.nome
    }
    set nomeAluno(nomeAluno) {
        this.nome = nomeAluno
    }
    get cursoAluno() {
        return this.curso
    }
    set cursoAluno(cursoAluno) {
        this.curso = cursoAluno
    }
    get semestreAluno() {
        this.semestre = this.semestreAluno
    }
    set semestreAluno(semestreAluno) {
        this.semestre = this.semestreAluno
    }
}

let amanda = new Aluno('')
amanda.nomeAluno = 'amanda'