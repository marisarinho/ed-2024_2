from func import*

while True:
    op=input('''
Escolha uma das opçoes:
1- Cadastrar pessoa  
2- Listar pessoas  
3- Apagar pessoa
4- Sair ''')
    if op=='1':
        cadastrar_pessoa()
    elif op == '2':
        lista= listar_pessoas()
        print(lista)
    elif op == '3':
        apagar_pessoa()
    else:
        print('fim')
        break