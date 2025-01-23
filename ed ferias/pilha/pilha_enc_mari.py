class No:
    def __init__(self,carga):
        self.carga = carga
        self.proximo = None

class Pilha:
    def __init__(self):
        self.__topo = None
        self.__tamanho = 0

    def __len__(self):
        return self.__tamanho
    
    def vazia(self):
        return self.__tamanho == 0
    
    def topo(self):
        assert not self.vazia(), 'pilha vazia'
        return self.__topo.carga
    
    def esvaziar(self):
        self.__topo = None
        self.__tamanho = 0
    
    def empilha(self,carga):
        novo = No(carga)
        novo.proximo = self.__topo
        self.__topo = novo
        self.__tamanho += 1
    

    def desempilha(self):
        assert not self.vazia(), 'pilha vazia'
        topo = self.topo()
        self.__topo = self.__topo.proximo
        self.__tamanho -= 1
        return topo

    def copia_invertida(self) -> "Pilha":
        """ Retorna uma copia invertida """
        atual = self.__topo
        invertida = Pilha()
        while atual:
            invertida.empilha(atual.carga)
            atual = atual.proximo
        return invertida

    def inverter(self) -> None:
        aux = self.copia_invertida()
        self.esvaziar()
        while not aux.vazia():
            self.empilha(aux.desempilha())

    def duplicar(self):
        """ 
        duplicar a pilha original, retornar a copia 
        """
        aux = self.copia_invertida()
        copia = Pilha()
        while not aux.vazia():
            copia.empilha(aux.desempilha())
        return copia

    def achar(self,num):
        """retorna True se encontrar o numero 
        na pilha, False se nao encontrar
        """
        assert not self.vazia(), 'pilha vazia'
        atual = self.__topo
        while atual is not None:
            if atual == num:
                return True
            atual = atual.proximo
        return False
                
    def intercalar(self, pilha2: "Pilha"):
        intercalada = Pilha()
        aux1 = self.copia_invertida()
        aux2 = pilha2.copia_invertida()
        if len(aux1) < len(aux2):
            menor = aux1
            maior = aux2
        else:
            menor = aux2
            maior = aux1
        for _ in range(len(menor)):
            intercalada.empilha(maior.desempilha())
            intercalada.empilha(menor.desempilha())
        while not maior.vazia():
            intercalada.empilha(maior.desempilha())

    def __str__(self) -> str:
        s = ""
        atual = self.__topo
        while atual:
            if s != "":
                s += ' -> '
            s += str(atual.carga)
            atual = atual.proximo

        return s

pilha = Pilha()
pilha.empilha(10)
pilha.empilha(20)
pilha.empilha(30)
pilha2 = pilha.duplicar()
print(pilha)