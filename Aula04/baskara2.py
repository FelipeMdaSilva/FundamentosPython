import math as mt #Importação da biblioteca math

def delta(a, b, c): #Função para calcular o valor de delta
    delta = mt.pow(b,2) - 4 * a * c
    return delta

def raizes(delta, a, b): #Função para calcular os valores das raizes
    raiz1 = (- b + mt.sqrt(delta)) / (2 * a)
    raiz2 = (- b - mt.sqrt(delta)) / (2 * a)
    saida = f" Raiz 1 = {raiz1:.2f}\n\tRaiz 2 = {raiz2:.2f}"
    return saida
try:
    #Entrada de dados
    print("--Aplicativo para  calcular as raizes de uma equação de 2°grau--")
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    print(f"Equação -> {a}x² + {b}x + {c} = 0")

    #Processamento de dados
    delta1 = delta(a,b,c)
    if delta1 < 0:
        print("Raizes impossiveis")
    else:
        dados = raizes(delta1, a, b)
        #Saída de dados
        print(f"As raizes da equação de 2° grau são:\n\t{dados}")
except ValueError:
        print("Digite valores válidos")
except ZeroDivisionError:
     print("Digite o valor de a diferente de zero")
