import time as t
#Apresentação do aplicativo
print("Aplicativo de controle fluxo carros \n Parque Nacional os Lençóis Maranhenses \n \n Bem-vindo ao aplicativo de controle de fluxo de carros!")
#Entrada de dados
fluxo = str(input("Digite o fluxo de carro (entrada/saida) \n ou sair para encerrar a aplicação: "))
if fluxo != "entrada" and fluxo != "saida":
    print("Erro: Por favor, digite 'entrada ou 'saida'")
elif fluxo == "sair":
    print ("Saindo do aplicativo.")
    
try:
    turistas = int(input("Digite o número de turistas: "))
    turistas = int(turistas)
except:
    print("Erro: Digite um número")

print(f"Entrada registrada em: {t.ctime(t.time())}\nEntrada de {turistas} turistas registrada")
print(f"Total de turistas no parque: {turistas}")

fluxo = str(input("Digite o fluxo de carro (entrada/saida) \n ou sair para encerrar a aplicação: "))
if fluxo != "entrada" and fluxo != "saida":
    print("Erro: Por favor, digite 'entrada ou 'saida'")

