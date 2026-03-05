#Entrada de dados
glicose = float(input("Digite a sua glicose: "))
#Processamento de dados
#Esrutura de controle de decisão IF ELIF ELSE
if glicose <= 100:
    saida = "Normal"
elif (glicose > 100) and (glicose <= 140):
    saida = "Elevado"
else:
    saida = "Diabetes"
#Saida de dados
print(f"Classificação: {saida}")
