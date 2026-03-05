#Declarar as variaveis
largura:float
comprimento:float
preco:float
area:float
valor:float
#Entrada de dados
largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
preco = float(input("Digite o preço do metro quadrado do terreno: R$ "))
#Processamento de dados
area = largura * comprimento
valor = preco * area
#Saida de dados
print(f"A área do terreno é de {area} m²")
print(f"O valor do terreno de R$ {valor}")
