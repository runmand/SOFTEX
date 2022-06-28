def calculadora():
    valor1 = float(input("Digite o primeiro número"))
    valor2 = float(input("digite o segundo número"))
    operation = int(
        input("A seguir, digite a opção de operação que você deseja\n 1-Soma\n 2-Subtração\n 3-Multiplicação\n 4-Divisão\n"))

    if operation == 1: #Soma
        print(f"O valor da soma foi: {valor1 + valor2}")
    elif operation == 2:
        print(f"O valor da subtração foi {valor1 - valor2}")
    elif operation == 3:
        print(f"o valor da multiplicação foi {valor1 * valor2}")
    elif operation == 4:
        print(f"o valor da divisão foi {valor1 / valor2}")
    else:
        print("o valor inválido")

    continuar = int(input("DESEJA CONTINUAR?\n 1-SIM\n 2-NÃO\n"))
    if continuar == 1:
        calculadora()
    elif continuar == 2:
        print("OBRIGADA...FINALIZANDO!")
    else:
        print("valor inválido!")


inicio = input("INICIALIZAR CALCULADORA?\n DIGITE SIM OU NAO\n")
inicio = inicio.lower()
if inicio == "sim":
    calculadora()
elif inicio == "nao":
    print("OBRIGADA...FINALIZANDO!")
else:
    print("INVÁLIDO... TENTE NOVAMENTE")