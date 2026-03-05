SENHA = 2002
contagem = 0
senha = int(input("Digite a senha: "))
while (senha!=SENHA):
    contagem += 1
    #FAÇA O LOOP
    senha = int(input("Senha inválida, tente novamente: "))
    if (contagem >= 2):
        print("Número de tentativas excedido")
        break
if contagem <= 2:
    print("Acesso permitido!")
else:
    print("Acesso negado!")
