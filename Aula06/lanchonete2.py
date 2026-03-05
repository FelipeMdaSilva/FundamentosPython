#-------Entrada de dados-------
codigo = input("Codigo do produto comprado: ")
quantidade = int(input("Quantidade comprada: "))
produtos = {"1": 5.00, "2": 3.50, "3": 4.80, "4": 8.90, "5": 7.32}
valor = quantidade * produtos[codigo]
print("Valor a pagar é de ", valor)