serial_produto = 0 # variável global que vai controlar o ID dos produtos

dados = {"produtos": [],
         "pedidos": []}

def gerar_id_produto()->int:
    global serial_produto
    serial_produto += 1
    return serial_produto

def ler_produto()->tuple:
    desc = input('Descrição do produto: ')  
    valor = float(input('Valor unitário: ')) 
    return desc, valor

def listar_produtos():
    print("Produtos cadastrados:")
    if not dados['produtos']:
        print("Nenhum produto cadastrado.")
    else:
        for produto in dados['produtos']:
            print(f"ID: {produto['id']}, Descrição: {produto['descricao']}, Valor: {produto['valor']:.2f}")
    print('--------')

def cadastrar_produto(descricao:str, valor:float):
    global dados
    dados['produtos'].append({
        'id': gerar_id_produto(),
        'descricao': descricao,
        'valor': valor}
    )

def pesquisar_produto(id:int)->dict:
    global dados
    for produto in dados['produtos']:
        if produto['id'] == id:
            return produto
    return None
