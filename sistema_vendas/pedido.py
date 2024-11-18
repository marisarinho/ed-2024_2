from save import abrir_json, salvar_produtos
from gerenciador_produtos import GerenciarProduto

# estrutura de dados para armazenar todos pedidos
colecao_pedidos = {} #chave=ID;valor=list(carrinho)
# variável controladora do serial do pedido
serial_num_pedido = 0

# carregando dados
dados = abrir_json()
gerenciador = GerenciarProduto(dados)
salvar_produtos(dados)

class Pedido:
    def __init__(self,repositorio_produtos,quant):
        self.repositorio_produtos = repositorio_produtos
        self.quant = quant
        self.colecao_pedidos = {}
        self.id_pedido = self.gerar_id_pedido()

    def gerar_id_pedido(self) -> int:
        global serial_num_pedido
        serial_num_pedido += 1
        return serial_num_pedido

    def fechar_pedido(self, carrinho:list)->int:
        self.colecao_pedidos[self.id_pedido] = carrinho  
        return self.id_pedido
    
    def __str__(self):
        return f"Pedido ID: {self.id_pedido}, Quantidade de Itens: {self.quant}"


    def exibir_pedido(self):
        print('======================================================')
        print(f"Pedido ID: {self.id_pedido}")
        print('======================================================')
        print('idProduto  | Descrição      | Preço Unit. | Quantidade')
        print('-----------  ---------------  ------------  ----------')
        total = 0
        for item in self.colecao_pedidos[self.id_pedido]:
            produto = self.repositorio_produtos.pesquisar(item[0])  # Buscar produto pelo ID
            if produto:
                print(f"   {produto.id:03d}       {produto.descricao:15s}    {produto.valor:10.2f}      {item[1]:3d}")
                total += produto.valor * item[1]

        print('======================================================')
        print(f"Valor total das suas compras: {total:.2f}")
        print('======================================================')




def add_produto_carrinho(carrinho:list, idProduto:int,quant:int):
    carrinho.append([idProduto,quant])
