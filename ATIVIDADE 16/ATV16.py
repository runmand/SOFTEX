print ("CALCULADORA")

def Calculadora(number1,number2, operation):
    if (operation == 1):
        result = number1 + number2
        return result
    if (operation == 2):
        result = number1 - number2
        return result
    if (operation == 3):
        result = number1 * number2
        return result
    if (operation == 4):
        if (number2 == 0):
            result ="NÃO EXISTE DIVISÃO POR 0"
            return result
        else:
            result = number1 / number2
            return result
    if (operation == 0 or operation >4)    :
        result = 0
        return result

number1 = float(input("Digite o primeiro número: "))        
number2 = float(input("Digite o segundo número: "))
operation = int(input("""Digite a Operação desejada:
                1 - Soma
                2 - Subtração
                3 - Multiplicação
                4 - Divisão\n"""))

final = Calculadora(number1, number2, operation)
print(f'O seu cálculo tem como resultado: {final}')
