#Declaração de variaveis
base:float
altura:float
area:float
perimetro:float
diagonal:float
#Entrada de dados
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a base a altura do retângulo: "))
#Processamento de dados
area = base * altura
perimetro = 2*base + 2*altura
diagonal = (base**2 + altura**2)**0.5
#Saida de dados
print(f"Area = {area:.3f}")
print(f"Perimetro = {perimetro:.3f}")
print(f"Diagonal = {diagonal:.3f}")
