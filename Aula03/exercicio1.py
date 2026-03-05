try: 
    #Entrada de dados
    dias = int (input("Digite o número de dias: "))
    #Processamento de dados
    anos = dias // 365
    mes = (dias % 365) // 30
    dia = (dias % 30) % 30
    #Saída de dados
    print(f"{anos} ano(s)")
    print(f"{mes} mes(es)")
    print(f"{dia} dia(s)")
except:
    print("Erro: Digite o quantidade de dias")
