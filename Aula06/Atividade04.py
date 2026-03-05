try:
    n = int(input("Quantas pessoas ? "))
    altura_min = int(input("Altura mínima (cm): "))
    altura_max = int(input("Altura máxima (cm): "))

    contador = 0

    for i in range(n):
        altura = int(input(f"Pessoa {i+1} - altura: "))

        if not (altura < altura_min or altura > altura_max):
            contador += 1

    print(f"Podem andar: {contador}")

except ValueError:
    print("Erro: Digite apenas números inteiros.")