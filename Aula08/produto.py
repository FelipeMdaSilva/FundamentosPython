class Produto:
    #Membros da classe
    #Campos ou atributos da classe
    nome:str
    preco:float
    quantidade:int

    def valor_total_estoque(self) -> float:
        return self.quantidade * self.preco
    
    def adicionar_produtos(self, quantidade) -> int:
        self.quantidade += quantidade

    def remover_produtos(self, quantidade) -> int:
        self.quantidade -= quantidade

    def saida_dados(self) -> str:
        return f"Nome do produto: {self.nome}\n\
\tValor de compr do produto: {self.preco}\n\
\tQuantidade em estoque: {self.quantidade}\n\
\tValor total em estoque: {self.valor_total_estoque()}"