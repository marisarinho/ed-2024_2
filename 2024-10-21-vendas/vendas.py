from pprint import pprint
from produto import *
from pedido import *

carregar_dados()
print(
    "Bem vindo ao nosso sistema de vendas! Aqui você poderá cadastrar produtos e fazer pedidos."
)
print()


# Inicio do programa
while True:
    print("--------")
    opcao = int(
        input(
            """Selecione uma das opções abaixo:
1 - Cadastrar produto.
2 - Listar produtos.  
3 - Fazer pedido.
4 - Pesquisar produtos.                     
5 - Sair.
"""
        )
    )
    print("--------")
    if opcao == 1:

        descricao, valor = ler_produto()

        cadastrar_produto(descricao, valor)

        print("Produto cadastrado!")
        print("--------")


    elif opcao == 2:
        listar_produtos()


    elif opcao == 3:

        carrinho=[]
        total_compras=0

        while True:
            listar_produtos()
            pedido = input(
                "Digite o Id para escolher um pedido ou digite 0(numero zero)para finalizar compra."
            )
            print("--------")

            if pedido == "0":
                print("Os produtos que voce comprou:")
                for prod in carrinho:
                    print(f"{prod['descricao']},R${prod['valor']:.2f}")
                print(f"Valor total das suas comprinhas:{total_compras:.2f}")
                print("--------")
                break

            else:
                for produto in dados["produtos"]:
                    if produto["id"] == int(pedido):
                        quant = int(input("Digite quantos produtos desse ID você deseja: "))
                        print("--------")
                        # chamando a função
                        
                        total_compras = fazer_pedido(quant, produto, carrinho, total_compras)

                        print(
                            f"{quant}x {produto['descricao']} adicionado ao carrinho."
                        )
                        print("--------")


    elif opcao == 4:
        id = int(input("Digite o id do produto"))
        retorno = pesquisar_produto(id)
        if retorno:
            print(
                f"Produto encontrado: {retorno['descricao']}, valor: {retorno['valor']:.2f}"
            )

        else:
            print("Produto não encontrado.")


    elif opcao == 5:
        print("Fim do programa.")
        print("--------")
        break