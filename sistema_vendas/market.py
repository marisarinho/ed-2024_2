from product import Produto
from item_pedido import ItemPedido
from pedido import Pedido
from gerenciador_produtos import GerenciadorProdutos

gp = GerenciadorProdutos()
gp.adicionar_produto(Produto("Cadeira", 100.0)) # codigo 1 atribuido
gp.adicionar_produto(Produto("Mesa", 200.0)) # codigo 2 atribuido
gp.adicionar_produto(Produto("Cama", 300.0)) # codigo 3 atribuido
print(gp)

cart = Pedido(1) # criando o pedido de id=1
cart.adicionar_item(gp.pesquisar(1), 2) # adiciona a cadeira ao carrinho
cart.adicionar_item(gp.pesquisar(2), 3) # adiciona a mesa ao carrinho
cart.mostrar_carrinho()

