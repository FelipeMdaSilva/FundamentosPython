import trianguloOOP as t

#Instanciação dos objetos da classe Triangulo
trianguloX = t.Triangulo()
trianguloY = t.Triangulo()
LADOA = "Lado A = "
LADOB = "Lado B = "
LADOC = "Lado C = "

#Entrada de dados
print("Digite as medidas do triângulo X")
trianguloX.lado_A = float(input(LADOA))
trianguloX.lado_B= float(input(LADOB))
trianguloX.lado_C = float(input(LADOC))
print("Digite as medidas do triângulo Y")
trianguloY.lado_A = float(input(LADOA))
trianguloY.lado_B = float(input(LADOB))
trianguloY.lado_C = float(input(LADOC))
#Saida de dados
print(f"Área do triangulo X: {trianguloX.area():.4f}")
print(f"Área do triangulo Y: {trianguloY.area():.4f}")
