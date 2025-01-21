class No:
    def __init__(self,carga):
        self.carga = carga
        self.prox = None

class Controle:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

class Lista:
    def __init__(self):
        self.__head = Controle()
    
    def __len__(self):
        """ retorna o tamanho da lista """
        return self.__head.tamanho
    
    def vazia(self):
        return self.__head.inicio == None
    
    def esvaziar(self):
        self.__head.tamanho = 0
        self.__head.inicio = None

    def elemento_frente(self):
        assert not self.vazia(),'lista vazia'
        return self.__head.inicio.carga
    
    def elemento(self,posicao):
        """retorna a carga armazenada na posição
           especificada como argumento"""
        assert not posicao

    def append(self,elem):
        """  insere elementos
         no fim da lista, replicando o append
           """
        if self.__head.inicio is not None:#se tiverem elementos ja na lista
            cursor = self.__head.inicio
            #percorrendo ate o ponteiro n ter mais proximo(no caso, qnd ele for None)
            while(cursor.prox):
                cursor = cursor.prox
            #qnd o while acaba, o ponteiro n tem mais proximo
            #portanto, essa linha muda o None para No(elem) [que seria o novo ultimo no]
            cursor.prox = No(elem)
            
        else:
            #primeiro elemento
            self.__head.inicio = No(elem)
        self.__head.tamanho+=1


lista = Lista()
lista.append(3)
lista.append(4)
print(len(lista))