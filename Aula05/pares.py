def clodoaldo(x):
    resultado = x + (x+2) + (x+4) + (x+6) + (x+8)
    print(f"Soma = {resultado  }")

x = 1

while (x!=0):
    x = int(input("Digite um numero inteiro: "))
    if x == 0:
        break

    if (x%2) == 0:
        print("Numero PAR")
        clodoaldo(x)
    else:
        print("Numero IMPAR")
        x += 1
        clodoaldo(x)
        