RESP1 = "Quantos casos você vai digitar? " #Váriavel constante
try:
    #Entrada de dados
    n = int(input(RESP1 ))
    for i in range(n):
        x = float(input("Digite o numerador: "))
        y = float(input("Digite o denominador: "))
        if (y == 0):
            #Saída de dados 1
            print("Divisão impossível")
        else:
            #Processamento de dados
            resultado = x / y 
            #Saída de dados 2
            print(f"Divisão = {resultado:.2f}")
except:
    print("Digite valores válidos!")