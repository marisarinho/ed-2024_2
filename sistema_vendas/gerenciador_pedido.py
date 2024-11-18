from pedido import Pedido

class GerenciadorPedido:
    def __init__(self):
        self.repositorio_pedidos = {}

    def adicionar_pedido(self, pedido:Pedido):
        self.repositorio_pedidos[pedido.id] = pedido

    def pesquisar_pedido(self,id_pedido):
        return self.repositorio_pedidos.get(id_pedido)

    def remover_pedido(self,id_pedido):
        if id_pedido in self.repositorio_pedidos:
            del self.repositorio_pedidos[id_pedido]
            return True
        return False
    
    def listar_pedidos(self):
        for pedido in self.repositorio_pedidos.values()
            print(pedido.exibir_pedido())