print("\n.NOTAS.\n")

nome = input("Digite o nome do aluno: ")
faltas = int(input("Digite o número de faltas do aluno: "))
nota_1 = float(input("Digite a primeira nota do aluno: "))
nota_2 = float(input("Digite a segunda nota do aluno: "))
media = (nota_1 + nota_2) / 2

print(f"""
Aluno: {nome}
Média: {media}
Faltas: {faltas}
""")

if media < 7 or faltas > 3:
    print("O aluno foi reprovado\n")
else:
    print("O aluno foi aprovado. Parabéns!\n")