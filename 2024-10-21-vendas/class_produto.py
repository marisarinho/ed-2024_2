#serial_produto = 0  # variável global que vai controlar o ID dos produtos

class Produto:
    def __init__(self, desc, valor, idProduto):
        self.desc = desc
        self.valor = valor
        self.idProduto = idProduto

    #sem o @staticmethod, o ler_produto nao funcionava no main
    #ele indica que ess metodo pertence a classe,nao a algum objeto dela

    @staticmethod
    def ler_produto() ->tuple:
        desc = input('Descrição do produto: ')
        valor = float(input('Valor unitário: '))
        return desc, valor

class GerenciarProduto:
    def __init__(self, dados): #nosso dic dados e, por consequencia, list produtos.
        self.dados = dados
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

    def pesquisar_produto(self, id: int) -> dict:
        for produto in self.dados['produtos']:
            if produto['id'] == id:
                return produto
        return {}