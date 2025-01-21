import numpy as np

class PilhaSeq:
    def __init__(self):
        self.__topo = -1
        self.__tamanho = 0
        self.__pilha = np.full(10,None)

    def empilha(self, carga):
        assert not self.cheia(), 'pilha cheia' 
        self.__pilha[self.__topo+1] = carga
        self.__tamanho += 1
        self.__topo += 1

    def vazia(self):
        return self.__tamanho == 0
    
    def cheia(self):
        return len(self.__pilha) == self.__tamanho

    def desempilha(self):
        assert not self.vazia(), 'pilha vazia'
        self.__topo -= 1
        self.__tamanho -= 1
        return self.__pilha[self.__topo+1]
    
    def __len__(self):
        return self.__tamanho
    
    def topo(self):
        assert not self.vazia(), 'pilha vazia'
        return self.__pilha[self.__topo]
    
    def __str__(self):
        string = 'topo -> ['
        for i in range(self.__tamanho):
            string += str(self.__pilha[i]) + ', '
        string = string.rstrip(', ')
        string += ']'
        return string
    

pilha = PilhaSeq()
pilha.empilha(3)
pilha.empilha(4)
pilha.empilha(5)
pilha.empilha(6)
print(pilha)