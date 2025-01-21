import numpy as np

class Pilha:
    def __init__(self, tamanho):
        self.__topo = -1
        self.__tamanho = 0
        self.__pilha = np.full(tamanho, None)

    def topo(self):
        assert not self.vazia(), 'pilha vazia sem topo'
        return self.__pilha[self.__topo]
    
    def __len__(self):
        return self.__tamanho
    
    def vazia(self):
        return self.__tamanho == 0 
    
    def cheia(self):
        return len(self.__pilha) == self.__tamanho
    
    def empilhar(self,carga):
        assert not self.cheia(),' pilha cheia'
        self.__pilha[self.__topo + 1] = carga
        self.__tamanho+=1
        self.__topo +=1

    def desempilha(self):
        assert not self.vazia(),'pilha vazia'
        self.__topo -= 1
        self.__tamanho-=1
        return self.__pilha[self.__topo + 1]



pilha = Pilha(10)

if pilha.cheia():
    print("Falhou no teste 1")
    exit()
print("Passou teste 1")


if pilha.topo() is None:
    print("Falhou no teste 1.5")
    exit()

print("Passou no teste 1.5")

try:
    pilha.desempilha()
    print("Falhou no teste 2")
    exit()
except AssertionError as e:
    print("Passou teste 2")
    
pilha.empilhar(2)
pilha.empilhar(3)

if pilha.topo() != 3:
    print("Falhou no teste 3")
    exit()
print("Passou no teste 3")

if pilha.desempilha() != 3:
    print("Falhou no teste 4")
    exit()
print("Passou no teste 4")

if pilha.topo() != 2:
    print("Falhou no teste 5")
    exit()
print("Passou no teste 5")
