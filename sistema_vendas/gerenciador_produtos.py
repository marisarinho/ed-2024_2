from product import Produto

class GerenciadorProdutos:
    def __init__(self):
        self.repositorio_produtos = {}

    
    def adicionar_produto(self, produto:Produto):
        self.repositorio_produtos[produto.id] = produto

    
    def pesquisar(self, id:int)->Produto:
        return self.repositorio_produtos.get(id)
    
    def remover(self, id:int)->Produto:
        return self.repositorio_produtos.pop(id,None)

    def __str__(self)->str:
        s = ''
        # {self.repositorio_produtos}"""
        for produto in self.repositorio_produtos.values():
            s += produto.__str__() + '\n'
        return s
    
    def __len__(self)->int:
        return len(self.repositorio_produtos)

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto)