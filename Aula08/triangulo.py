LADOA = "Lado A = "
LADOB = "Lado B = "
LADOC = "Lado C = "

#Entrada de dados
print("Digite as medidas do triângulo X")
ax = float(input(LADOA))
bx = float(input(LADOB))
cx = float(input(LADOC))
print("Digite as medidas do triângulo Y")
ay = float(input(LADOA))
by = float(input(LADOB))
cy = float(input(LADOC))
#Processamento de dados
px = (ax + bx + cx) / 2
py = (ay + by + cy) / 2
areax = (px * (px - ax) * (px - bx) * (px - cx))**0.5
areay = (px * (py - ay) * (py - by) * (py - cy))**0.5
#Saida de dados
print(f"Área do triangulo X: {areax:.4f}")
print(f"Área do triângulo Y: {areay:.4f}")