"""
lista sequencial

class Lista:
    def __init__(self, capacidade):
        self.__array = np.full(capacidade,None)
        self.__ultimo = -1
"""
def insere_ordenado(self,carga):
    assert not self.estacheia(),'lista cheia'
    if self.estavazia():
        self.inserir(1,carga)
    for i in range(len(self)):
        if carga < self.__array[i]:
            self.inserir(i+1,carga)
            return
    self.inserir(len(self)+1,carga)
