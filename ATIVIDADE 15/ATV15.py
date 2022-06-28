import time

print("\nBOMBA!!!!!!!!!!!!!!!!!!!!!!!!\n")

segundos = int(input("Digite o número de segundos até a bomba explodir "))

print("\nCONTAGEM REGRESSIVA\n")

for i in range(segundos, 0, -1):
    print(i)
    time.sleep(2)

print("\nBooooooooOOOOOOOOOOOOOOOoooooooooooooooM!\n")