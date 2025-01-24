from pilha_enc_mari import Pilha

"""(Mostra a pasta atual)
1. Entrar em uma pasta
	-> Pede para a pessoa dizer o nome da pasta
2. Voltar para a pasta anterior
	-> Não precisa pedir nada ao usuario
3. Voltar para a primeira pasta
	-> Tbm não precisa pedir nada ao usuario
4. Sair"""

pilha = Pilha()

while True:
    print("""
             1. Entrar em uma pasta
             2. Voltar para a pasta anterior
             3. Voltar para a primeira pasta
             4. Printar
             5. Sair
          """)
    escolha = int(input('Escolha uma opçao: '))

    if escolha == 1:
        pasta = input('digite o nome da pasta: ')
        pilha.empilha(pasta)
    elif escolha == 2:
        pilha.desempilha()
    elif escolha == 3:
        while len(pilha) != 1:
            pilha.desempilha()
    elif escolha == 4:
        print(pilha.copia_invertida())
    elif escolha == 5:
        pilha.esvaziar()
        print('programa encerrado')
        break