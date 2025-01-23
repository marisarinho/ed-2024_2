"""Considere que vamos implementar algumas funcionalidades de um browser. Para isso, vamos
precisar de uma Pilha para controlar o histórico de páginas visitadas. Neste cenário, a classe DNS
apresentada a seguir permite adicionar e verificar se uma url é válida ou não.(5,0 pontos)
class DNS:
__urls={“ifpb”:“192.168”, “google”: “10.10”, “g1”: “19.17”, “uol”:”1.10”}
@classmethod
def add(cls, url:str, ip:str):
cls.__urls[url] = ip
@classmethod
def existsURL(cls, url:str)->bool:                                        
return url in cls.__urls.keys()

A classe Browser tem a seguinte estrutura:
from Pilha import Pilha
class Browser:
def __init__(self):
self.__historico = Pilha()
self.__home = None
def request(self, url:str)->bool:
pass
def back(self):
pass
def __str__(self):
pass
"""

"""safari = Browser()
print(safari)
[ ]
home: None
safari.request(“google”)
safari.request(“ifpb”)
safari.request(“uol”)
safari.request(“record”)
print(safari)
[ google > ifpb ]
home: uol
safari.request(“g1”)
safari.request(“tsi”)
print(safari)
[ google > ifpb > uol ]
home: g1
safari.back()
safari.back()
print(safari)
[ google ]
home: ifpb
"""

"""Na lógica do cenário ilustrado, há métodos que precisam ser implementados. Implemente os
médicos da classe Browser para que atendam aos seguintes requisitos:
a) Quando o browser é instanciado, não haverá nenhuma página acessada. Logo o home é vazio
(none). O home representa a página que está aberta no momento. Toda vez que for feita uma
requisição para exibição de uma página, por meio do método request(), se a página existir, esta
passará a ser o home, enquanto a página anterior tem que ser gerenciada pelo histórico.
b) O método back() carrega no browser a última página visitada. Se não houver página a ser
retornada, permanece no home atual.
c) O método __str__() deve retornar o histórico de páginas visitadas no seguinte formato:
google > ifpb > uol
home: g1
As operações básicas da Pilha que estão disponíveis são as seguintes: estaVazia(),__len__(),
__str__(), elemento(), busca(), desempilha(), empilha( ) e topo( )."""
class DNS:
    __urls= {“ifpb”:“192.168”, “google”: “10.10”, “g1”: “19.17”, “uol”:”1.10”}
    @classmethod
    def add(cls, url:str, ip:str):
        cls.__urls[url] = ip
    @classmethod
    def existsURL(cls, url:str)->bool:                                        
        return url in cls.__urls.keys()
    
class Browser:
    def __init__(self):
        self.__historico = Pilha()
        self.__home = None
    def request(self, url:str)->bool:
        pass
    def back(self):
        if not self.__historico.estaVazia():
            antes = self.__historico.desempilha()
            self.__home = antes
        else:
            
    def __str__(self):
        pass