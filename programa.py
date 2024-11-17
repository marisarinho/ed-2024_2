import os
import subprocess
import platform
from git import GitMari

def limpar_terminal() -> None:
    if platform.system() == "Windows" and os.getenv("TERM") != "xterm":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

git = GitMari()

while True:
    limpar_terminal()
    print('''
Oq vc deseja fazer?
1 - Git Init
2 - Git Add
3 - Git Push
4 - Git Commit
5 - Git Checkout
6 - Git Pull
7 - Git Clone
8 - Git Status
9 - Sair
''')
    opcao = input('> ')
    if opcao == '1':
        git.init()
    elif opcao == '2':
        git.add()
    elif opcao == '3':
        nome_branch = input('Nome da branch: ') 
        git.push(nome_branch)
    elif opcao == '4':
        descricao_alteracoes = input('Descreva suas alteraçoes: ')
        git.commit(descricao_alteracoes)
    elif opcao == '5':
        nome_branch = input('Nome da branch: ') 
        git.checkout(nome_branch)
    elif opcao == '6':
        nome_branch = input('Nome da branch: ')
        git.pull(nome_branch)
    elif opcao == '7':
        url = input('Digite a url: ')
        git.clone(url)
    elif opcao == '8':
        git.status()
    elif opcao == '9':
        print('Fim do programa.')
        break
    input('aperte enter para continuar no programa...')
    