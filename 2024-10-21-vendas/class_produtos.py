#serial_produto = 0  # variável global que vai controlar o ID dos produtos

class Produto:
    def __init__(self, desc, valor, idProduto):
        self.desc = desc
        self.valor = valor
        self.idProduto = idProduto

    #sem o @staticmethod, o ler_produto nao funcionava no main
    #ele indica que ess metodo pertence a classe,nao a algum objeto dela

def ler_produto() ->tuple:
        desc = input('Descrição do produto: ')
        valor = float(input('Valor unitário: '))
        return desc, valor
