



n = int(input("Digite o número de altura das pessoas: "))
altura_minima = int(input("Digite a altura minima (cm): "))
altura_maxima = int(input("Digite a altura maxima(cm): "))

contador = 0

for i in range(1, n + 1):
    try:
        numero = i
        altura = int(input("Digite a altura da pessoa " + str(numero) + " (em cm): "))
        
        if altura >= altura_minima and altura <= altura_maxima:
            contador = contador + 1

    except ValueError:
        print("Erro:digite apenas números em centímetros!")
        break #error

print("Quantidade de pessoas que podem andar:", contador)