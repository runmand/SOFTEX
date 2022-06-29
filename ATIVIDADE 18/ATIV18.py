print("\nCALCULADORA DE NASCIMENTO\n")

def start_name():
    name = input("Digite o seu nome: ")
    if len(name) > 2:
        return name
    else:
        raise Exception("Digite um nome válido")

def start_year():
    
    ano = int(input("Digite o ano de seu nascimento: "))
    if year >= 1922 and year <= 2022:
        age = 2022 - year
        return age

    else:
        raise Exception("Ano de nascimento fora do aceito (1922-2022)")

def start_data():
    name = start_name()
    if len(name) > 0:
        age = start_year()
        print(f"\nSeu nome é {name}, você tem {age} anos\n")

while True:
    try:
        start_data()
        break
    except Exception as err:
        print(f"\nOcorreu um erro\n{err}\n")