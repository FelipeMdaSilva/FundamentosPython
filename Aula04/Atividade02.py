try:
    #Entrada de dados
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    #Esrutura de controle de decisão IF ELSE
    if (a + b > c) and (a + c > b) and (b + c > a):
        print(f"Perimetro = {a + b + c:.2f}")
    else:
        print(f"Area = {((a + b) * c) / 2:.2f}")
except:
    print("Erro: Digite um valor válido")
    