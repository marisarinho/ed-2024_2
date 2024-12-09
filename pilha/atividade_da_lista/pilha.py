import numpy as np

class Pilha:
    def __init__(self, tamanho:int=10):
        self.__elementos = np.full(tamanho,None)
        self.__topo = -1
    
    def empilha(self, carga):
        if self.__topo < len(self.__elementos)-1:
            self.__topo+=1 
            self.__elementos[self.__topo]=carga
        else:
            print('a pilha esta cheia')
        
    def desempilha(self):
        if self.__topo!= -1:
            valor = self.__elementos[self.__topo]
            self.__topo-=1
            return valor
        else:
            print('a pilha esta vazia')

    def __len__(self):
        return self.__topo + 1
    
    def topo(self):
        return self.__elementos[self.__topo]
    
    def esta_vazia(self):
        if self.__topo==-1:
            return True
        else:
            return False
        
    def esvaziar(self):
        if self.esta_vazia():
           print('pilha ja esta vazia')
           return False
        else:
            self.__topo = -1 
            return True
        
    def itens(self):
        return self.__elementos[:self.__topo + 1]

    def inverter(self):
        aux = Pilha()
        aux2 = Pilha()
        while not self.esta_vazia():
            aux.empilha(self.desempilha())
        while not aux.esta_vazia():
            aux2.empilha(aux.desempilha())
        while not aux2.esta_vazia():
            self.empilha(aux2.desempilha())

    def concatenar(self,pilha2):
        pilha2.inverter()
        while not pilha2.esta_vazia():
            self.empilha(pilha2.desempilha())

    def _transfere_elementos(pilha, pilha_final):
        pilha_aux1 = Pilha()
        pilha_aux2 = Pilha()
        while not pilha.esta_vazia():
            pilha_aux1.empilha(pilha.desempilha())
            pilha_aux2.empilha(pilha_aux1.topo())
        while not pilha_aux2.esta_vazia():
            pilha_final.empilha(pilha_aux2.desempilha())
            pilha.empilha(pilha_aux1.desempilha())

    @classmethod
    def concatena_pilha(cls, pilha1:"Pilha", pilha2:"Pilha")->"Pilha":
        pilha_final = Pilha()
        # se fosse um self, seria normal(self._nome da funcao)
        cls._transfere_elementos(pilha1, pilha_final)
        cls._transfere_elementos(pilha2, pilha_final)
        return pilha_final

    def __str__(self):
        s = '' 
        for i in range(self.__topo+1):
            s += f"{' <- ' if s != '' else ''}{self.__elementos[i]}"
        return s
    
pilha1 = Pilha()
pilha2 = Pilha()
pilha1.empilha(2)
pilha1.empilha(3)
pilha1.empilha(4)
pilha2.empilha(5)
pilha2.empilha(6)
pilha2.empilha(7)
pilha3 = Pilha.concatena_pilha(pilha1, pilha2)
print(pilha3)
