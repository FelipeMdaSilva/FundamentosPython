lista = []
contagem = 0
#-------------Entrada de dados------------
n = int(input("Quantos números vc vai digitar? "))
for i in range(n):
    numero = int(input("Digite um número: "))
    lista.append(numero)
print("Numeros pares: ", end=" ")
for i in range(len(lista)):
    if (lista[i] % 2) == 0:
        print(lista[i], end=" ")
        contagem+=1
print(f"\nQuantidade de pares: {contagem}")