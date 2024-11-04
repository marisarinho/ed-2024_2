from save import abrir_json, salvar_produtos
from class_produto import GerenciarProduto

# estrutura de dados para armazenar todos pedidos
colecao_pedidos = {} #chave=ID;valor=list(carrinho)
# variável controladora do serial do pedido
serial_num_pedido = 0


# carregando dados
dados = abrir_json()
gerenciador = GerenciarProduto(dados)
salvar_produtos(dados)

def gerar_id_pedido() -> int:
    global serial_num_pedido
    serial_num_pedido += 1
    return serial_num_pedido

def fechar_pedido(colecao_pedidos:dict, carrinho:list)->int:
    id_pedido = gerar_id_pedido()
    colecao_pedidos[id_pedido] = carrinho
    
    return id_pedido

def add_produto_carrinho(carrinho:list, idProduto:int,quant:int):
    carrinho.append([idProduto,quant])

def exibir_pedido(carrinho:list):
    print('======================================================')
    print("                 Itens do pedido:")
    print('======================================================')
    print('idProduto  | Descrição      | Preço Unit. | Quantidade')
    print('-----------  ---------------  ------------  ----------')
          
    total = 0
    for item in carrinho:
        produto = gerenciador.pesquisar_produto(item[0])        
        print(f"   {produto['id']:03d}       {produto['descricao']:15s}    {produto['valor']:10.2f}      {item[1]:3d}")
        total += produto['valor'] * item[1]

    print('======================================================')
    print(f"Valor total das suas comprinhas:{total:.2f}")
    print('======================================================')