class No:
    def __init__(self,carga):
        self.esquerda = self.direita = None
        self.carga = carga

    def __str__(self):
        return str(self.carga)
"""
7) Adicione à sua biblioteca de árvores binárias um método que determine
 qual o nível em que uma chave
key de busca é encontrada na árvore. Se não for encontrada, devolve 0 (zero). 
O protótipo da função
pode ser dado por:
def getLevel(self, key):

  """  
class ArvoreBinaria:
    def __init__(self,carga=None):
        self.tamanho = 0
        if carga is not None:
            self.raiz = No(carga)
            self.tamanho = 1
        else:
            self.raiz = None
            self.tamanho = 0
        self.cursor = self.raiz

    def criar_raiz(self,carga):
        if self.raiz is not None:
            raise Exception('raiz ja existente')
        else:
            self.raiz = No(carga)
            self.cursor = self.raiz
            self.tamanho = 1
    
    def esta_vazia(self):
        return self.tamanho == 0
        #return self.raiz == None

    def get_raiz(self):
        return self.raiz
    
    def get_cursor(self):
        return self.cursor.carga
    
    def desce_esquerda(self):
        if self.cursor is None or self.cursor.esquerda is None:
            return
        self.cursor = self.cursor.esquerda 

    def desce_direita(self):
        if self.cursor is None or self.cursor.direita is None:
            return
        self.cursor = self.cursor.direita

    def add_esq(self,carga):
        assert not self.esta_vazia(), 'arvore sem raiz'
        assert self.cursor.esquerda is None, 'ja tem filho esquerdo'
        self.cursor.esquerda = No(carga)
        self.tamanho+=1
    
    def add_dir(self,carga):
        assert not self.esta_vazia(), 'arvore sem raiz'
        assert self.cursor.direita is None, 'ja tem filho direito'
        self.cursor.direita = No(carga)
        self.tamanho+=1
        
    def __pos_ordem(self,raiz):
        if raiz is not None:
            self.__pos_ordem(raiz.esq)
            self.__pos_ordem(raiz.dir)
            print(raiz.carga,end=' ')
    def pos_ordem(self):
        self.__pos_ordem(self.raiz)

    def __pre_ordem(self,raiz):
        if raiz is not None:
            print(self.raiz,end=' ')
            self.__pre_ordem(raiz.esq)
            self.__pre_ordem(raiz.dir)
    def pre_ordem(self):
        self.__pre_ordem(self.raiz)

    def __em_ordem(self,raiz):
        if raiz is not None:
            self.__pre_ordem(raiz.esq)
            print(self.raiz,end=' ')
            self.__pre_ordem(raiz.dir)
    def em_ordem(self):
        self.__em_ordem(self.raiz)

    def __len__(self):
        return self.tamanho
    
    def altura(self):
        return self.__altura(self.raiz)
    def __altura(self,raiz):
        """
    1 no = 2^0(altura 0)
    2 nos = 2^1(altura 1)
    4 nos = 2^2(altura 2)
    8 nos = 2^3(altura 3)
    
    """
        if raiz is None:
            return -1 
        esq = self.__altura(raiz.esq)
        direita = self.__altura(raiz.dir)
        if esq>direita:
            return 1 + esq
        return 1+ direita
    
    def count(self):
        return self.__count(self.raiz)
    def __count(self,raiz):
        if raiz is None:
            return 0
        return 1+ self.__count(raiz.esq)+ self.__count(raiz.dir)
    
    def __leafs(self, no):
        if no is None:
            return 0
        if no.esq is None and no.dir is None:        
            return 1 
        
        return self.__leafs(no.esq) + self.__leafs(no.dir)
    
        """
        7) Adicione à sua biblioteca de árvores binárias um método que determine
        qual o nível em que uma chave
        key de busca é encontrada na árvore. Se não for encontrada, devolve 0 (zero). 
        O protótipo da função
        pode ser dado por:
        def getLevel(self, key):
        """
