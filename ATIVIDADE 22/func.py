class Funcionarios:

    def __init__(self, nome, setor):
        self.nome = nome
        self.setor = setor

    def info(self):
        print(self.nome,self.setor)

funcionario1 = Funcionarios("Amanda", "Frontend")
funcionario2 = Funcionarios("Natalia", "RH")
funcionario3 = Funcionarios("Beatriz", "Contabilidade")

funcionario1.info()
funcionario2.info()
funcionario3.info()