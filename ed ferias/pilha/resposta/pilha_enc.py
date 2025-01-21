class No:
    def __init__(self,carga):
        self.__proximo = None
        self.__carga = carga

    @property
    def carga(self):
        return self.__carga
    
    @carga.setter
    def carga(self, carga):
        self.__carga = carga
    #vira tipo um metodo mas pega de jeito diferente 
    #no.carga = 3
    #normalmente vc pega assiim no.carga(3)
    #msma coisa pra printar print(no.carga)  sem ()

    @property
    def proximo(self):
        return self.__proximo

    @proximo.setter
    def proximo(self, no):
        self.__proximo = no

class Pilha:
    def __init__(self):
        self.__topo = None
        self.__tamanho = 0

    def __len__(self):
        """ Retorna o tamanho """
        return self.__tamanho

    def vazia(self):
        """ Retorna true se tiver vazia """
        return self.__tamanho == 0 

    def topo(self):
        """ Retorna o valor que está no topo da pilha """
        assert not self.vazia(), 'pilha vazia'
        return self.__topo.carga

    def empilha(self,carga):
        """ Coloca um valor no topo da pilha """
        novo = No(carga)
        novo.proximo = self.__topo
        self.__topo = novo

    def desempilha(self):
        """ Tira um valor do topo da pilha e retorna ele """
        topo = self.topo()
        self.__topo = self.__topo.proximo
        return topo
    
    # def __str__(self):
        