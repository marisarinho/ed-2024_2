
from class_produtos import*
from save import*

class GerenciarProduto:
    def __init__(self): #nosso dic dados e, por consequencia, list produtos.
        self.dados = {'produtos':[]}
        self.serial_produto = 1

    #consertar!!!!
    def gerar_id_produto(self) -> int:
        idProduto = self.serial_produto
        self.serial_produto += 1
        return idProduto

    def listar_produtos(self):
        print("Produtos cadastrados:")
        #remover a amarração do código!
        if not self.dados['produtos']:
            print("Nenhum produto cadastrado.")
        else:
            for produto in self.dados['produtos']:
                print(f"ID: {produto['id']}, Descrição: {produto['descricao']}, Valor: {produto['valor']:.2f}")
        print('--------')

    def cadastrar_produto(self, descricao: str, valor: float):
        produto_id = self.gerar_id_produto()
        self.dados['produtos'].append({
            'id': produto_id,
            'descricao': descricao,
            'valor': valor
        })
        
        salvar_produtos(self.dados)

    def pesquisar_produto(self, id: int) -> dict:
        for produto in self.dados['produtos']:
            if produto['id'] == id:
                return produto
        return {}