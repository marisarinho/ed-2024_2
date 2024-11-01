import json

serial_produto = 0 # variável global que vai controlar o ID dos produtos

def abrir_json() ->dict:
    try:
        with open('produtos.json', 'r') as arquivo_json:
            produtos_json = json.load(arquivo_json)
            #se o dic estiver vazio
            if produtos_json == {}:
                return {'produtos':[], 'pedidos':[]}
            
            #nessa de baixo, retorna o dicionario normalmente
            return produtos_json
        #caso nao exista esse arquivo, ou caso o json esteja totalmente vazio
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {'produtos':[], 'pedidos':[]}
    

     # A gente não tá criando o arquivo, tá só atribuindo esse valor default pra dados.
    # Se a gente usasse abrir_json mais de uma vez no código, ia dar problema, 
    # porque toda vez que o arquivo não existisse, ele ia retornar esse default
    # {'produtos': [], 'pedidos': []} sem realmente criar o arquivo. Isso significa
    # que qualquer dado novo não seria salvo se o arquivo não existisse ainda.
    # Pra resolver isso, podia garantir que o arquivo fosse criado logo na inicialização.
    

def salvar_produtos(produtos ):
    with open('produtos.json', 'w') as arquivo_json:
        json.dump(produtos, arquivo_json, indent=4)

dados = abrir_json()


def gerar_id_produto() -> int:
    global serial_produto, dados
    if dados['produtos']:
        serial_produto = dados['produtos'][-1]['id']
        serial_produto += 1
    else:
        serial_produto = 1
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
