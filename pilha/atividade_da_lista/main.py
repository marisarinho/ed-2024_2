from pilha import Pilha

pilhas = [Pilha() for _ in range(10)]
pilha_selecionada = 0

while True:
    print('''Editor de Pilha v1.2
=====================================''')
    print(f'''Pilha Selecionada:{pilha_selecionada + 1} de {len(pilhas)}
            [{pilhas[pilha_selecionada]}] <- topo
''')
    print('''
=====================================
(e) Empilhar
(d) Desempilhar
(t) Tamanho
(o) Obter elemento do topo
(v) Teste de pilha vazia
(r) Criar nova Pilha
(n) Inverter os elementos da pilha
(z) Esvaziar a pilha
(c) Concatenar duas pilhas
(m) Escolher outra pilha
(n) Conversão dec/bin
(s) Sair
=====================================
''')
    
    op = input('Digite sua opção: [ _ ]')
    if op=='e':
        #como fzr operaçao normal
        #chamar metodo ou instanciar aqui direto?
        pass
    if op =='d':
        pass
    if op == 's':
        print('Fim do programa.')
        break 
