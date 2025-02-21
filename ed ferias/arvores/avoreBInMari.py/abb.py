class No:
    def __init__(self,carga):
        self.carga = carga
        self.esquerda = None
        self.direita = None
    
    def __str__(self):
        return str(self.carga)

class ABB:
    def __init__(self):
        self.raiz = None
    
    def inserir(self,carga):
        if self.raiz is None:
            self.raiz = No(carga)
        else:
            self.__inserir(self.raiz, carga)
    def __inserir(self,no,carga):
        if carga < no.carga:
            if no.esquerda is None:
                no.esuqerda = No(carga)
            else:
                self.__inserir(no.esquerda, carga)
        else:
            if no.direita is None:
                no.direita = No(carga)
            else:
                self._inserir_recursivo(no.direita, carga)