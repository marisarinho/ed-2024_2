class Produto:
    # método especial denominado "construtor", que é rodado
    # implicitamente toda vez que uma instrução de criação
    # de objeto é encontrado
    def __init__(self, id:int, descricao:str, valor:float):
        self.descricao = descricao
        self.valor = valor
        self.id = id

    def get_descricao(self)->str:
        return self.descricao
    
    def get_valor(self)->float:
        return self.valor
    
    def set_preco(self, percentual:float):
        if percentual > 0.0:
            self.valor += self.valor * percentual / 100

    def __str__(self)->str:
        return f""" PRODUTO DISPONÍVEL
        Id: {self.id}
        Produto: {self.descricao}
        Valor: {self.valor:.2f}"""
