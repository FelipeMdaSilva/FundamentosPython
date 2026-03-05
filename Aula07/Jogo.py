import random

print("========Jogo de adivinhar número!========")

while True:
    numero_aleatorio = random.randint(1, 10)
    tentativas = 0

    while True:
        try:
            palpite = int(input("Informe o número aleatório (1 a 10): "))
            tentativas += 1

            if palpite < 1 or palpite > 10:
                print("Número inválido: digite um número de 1 a 10")
                continue

            if palpite > numero_aleatorio:
                print("Muito alto! Tente novamente.")

            elif palpite < numero_aleatorio:
                print("Muito baixo! Tente novamente.")

            else:
                print(f"Parabéns, você acertou em {tentativas} tentativa(s)! \nO número sorteado era {numero_aleatorio}")
                break

        except ValueError:
            print("ERRO! Digite apenas números.")

    resposta = input("Deseja jogar novamente? (s/n): ")

    if resposta == "n":
        print("Obrigado por jogar, até a próxima!")
        break