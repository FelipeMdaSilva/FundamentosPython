import produto as p #Importando o módulo produto e dando a ele o apelido de p, para facilitar a escrita do código

#Criar objeto do tipo Produto
play = p.Produto()

#Entrada de dados
print("Entre os dados do produto: ")
play.nome = input("Nome: ")
play.preco = float(input("Preço: R$"))
play.quantidade = int(input("Quantidade: "))

#Saida de dados
print("Dados do produto: ")
print(play.saida_dados())

#Saida de dados n°2
quantidade = int(input("Digite a quantidade a ser adicionado ao estoque: "))
print("Dados atualizados: ")
play.adicionar_produtos(quantidade)
print(play.saida_dados())

#Saida de dados n°3
quantidade = int(input("Digite a quantidade a ser removida ao estoque: "))
print("Dados atualizados: ")
play.remover_produtos(quantidade)
print(play.saida_dados())