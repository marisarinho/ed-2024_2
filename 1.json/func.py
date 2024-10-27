import json
import os

def carregar_dados():
    if os.path.exists("dados.json"):
        with open("dados.json", "r") as arquivo:
            return json.load(arquivo)
    return [] 

def salvar_dados(dados):
    with open("dados.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=3)

def listar_pessoas():
    dados=carregar_dados()
    if dados:
        for pessoa in dados:
            print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}")
    else:
        print('nenhum cadastro')

def apagar_pessoa():
    listar_pessoas()
    dados=carregar_dados()
    tirar_pessoa=input('quem vc quer tirar?')
    if dados:
        for pessoa in dados:
            if tirar_pessoa==pessoa['nome']:
                dados.remove(pessoa)
                salvar_dados(dados)
                print(f"{tirar_pessoa} foi removido(a) com sucesso!")
                return
        print('nome nao encontrado')
    else:
        print('nada pra remover ainda')


def cadastrar_pessoa():
    dados = carregar_dados()
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    dados.append({"nome": nome, "idade": idade})
    salvar_dados(dados)
    print("Dados salvos com sucesso!")
