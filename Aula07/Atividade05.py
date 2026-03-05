n = int(input("Digite a quantidade de competidores: "))

for i in range(n):
    nome = input(f"Digite o nome do competidor {i+1}: ")
    grau = float(input(f"Digite o grau de dificuldade de {nome} (1.2 a 3.8): "))
    notas = list(map(float, input(f"Digite as 7 notas de {nome} separadas por espaço: ").split()))
    
    notas.remove(max(notas))
    notas.remove(min(notas))
    
    soma = sum(notas)
    resultado = soma * grau
    
    print(f"{nome} {resultado:.2f}")