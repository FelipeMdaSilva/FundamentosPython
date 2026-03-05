#Entrada de dados
n = int(input("Deseja a tabuada de qual valor? "))
for i in range(10):
    print(f"{n} X {i+1} = {n * (i+1)}")
    