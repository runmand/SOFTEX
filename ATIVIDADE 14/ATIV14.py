print("\n.VEÍCULOS.\n")

quantidade_de_rodas = int(input("Digite a quantidade de rodas do veículo: "))
peso_bruto = float(input("Digite o peso do veículo em KG: "))
quantidade_de_pessoas = int(input("Digite a quantidade de pessoas que cabem no veículo: "))

habilitacao = ""
erro = False

if quantidade_de_rodas == 3 or quantidade_de_rodas == 2:
    habilitacao = "A"
elif quantidade_de_rodas == 4 and quantidade_de_pessoas <= 8 and peso_bruto <= 3500:
    habilitacao = "B"
elif quantidade_de_rodas >= 4 and peso_bruto > 3500 and peso_bruto <= 6000:
    habilitacao = "C"
elif quantidade_de_rodas >= 4 and quantidade_de_pessoas> 8:
    habilitacao = "D"
elif quantidade_de_rodas >= 4 and peso_bruto > 6000:
    habilitacao = "E"
else:
    erro = True

if erro:
    print("\n.ERRO. TENTE NOVAMENTE!\n")
else:
    print(f"\n A sua habilitação indicada é: {habilitacao}\n")