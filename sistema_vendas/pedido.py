from product import Produto
from item_pedido import ItemPedido
from pilha_encadeada import Pilha

class Pedido:
    def __init__(self, id:int):
        self.id = id # id do pedido
        self.itens = [] # dicionario com os itens de pedido
        # Essa lista sao os itens que o pedido vai ter ok?segue explicando 
    
    def adicionar_item(self, produto:Produto, quantidade:int):
        self.itens.append(ItemPedido(produto, quantidade))
        

    def total_pedido(self):
        total = 0
        for item in self.itens:
            total += item.total_item()
        return total
    
    def mostrar_carrinho(self): 
        print('======================================================')
        print("                 Itens do pedido:")
        print('======================================================')
        print('idProduto  | Descrição      | Preço Unit. | Quantidade ')
        print('-----------  ---------------  ------------  ----------')
        pilha = Pilha()
        for item in self.itens:
            pilha.empilha(item)

        while not pilha.vazia():
            item = pilha.desempilha()
            print(f'    {item.produto.id:3d}      {item.produto.descricao:15s}     {item.produto.valor:9.2f}      {item.quantidade:3d}')  
        print('======================================================')
        print(f"Valor total das suas comprinhas: R$ {self.total_pedido():.2f}")
        print('======================================================')
    
    def __str__(self):
        return f"Pedido: {self.id} | Total: {self.total_pedido():.2f}"