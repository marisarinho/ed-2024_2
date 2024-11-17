'''
metodos do git: 
git init
git add .
git push origin nomeDaBranch
git commit -m "Descrição das alterações"
git checkout nomeDaBranch
git pull origin nomeDaBranch
git clone url
git status
'''
class GitMari:
    def __init__(self) -> None:
        pass
    
    def init(self):
        print('git init')
        print('inicializou um repositorio.')

    def add(self):
        print('git add . ')
        print('adicionou arquivos prontos pra ser comitados.')

    def push(self, nome_branch:str):
        print(f'git push origin {nome_branch}')
        print('enviou commits locais para o repositorio.')

    def commit(self,descricao_alteracoes:str):
        print(f'git commit -m {descricao_alteracoes}')
        print('commitou!!')

    def checkout(self,nome_branch:str):
        print(f'git checkout {nome_branch}')
        print('alternou entre branches.')
    
    def pull(self,nome_branch:str):
        print(f'git pull {nome_branch}')
        print('atualizou o repositorio local com as mudanças do remoto.')

    def clone(self,url:str):
        print(f'git clone {url}')
        print('clonou o repositório.')

    def status(self):
        print('git status')
        print('mostrou o estado do repositorio atual.')