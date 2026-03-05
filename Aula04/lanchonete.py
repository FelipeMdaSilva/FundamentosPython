#Entrada de dados
codigo = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))
#Processsamento de dados - Estrutura de controle match-case
match codigo:
    case 1:
        #R$ 5.00
        total = quantidade * 5.00
    case 2:
        #R$ 3.50
        total = quantidade * 3.50
    case 3:
        #R$ 4.80
        total = quantidade * 4.80
    case 4: 
        #R$ 8.90
        total = quantidade * 8.90
    case 5:
        #R$ 7.32
        total = quantidade * 7.32
#Saida de dados
print(f"Valor a pagar = {total:.2f}")
