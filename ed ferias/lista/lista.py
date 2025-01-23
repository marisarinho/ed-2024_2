class ListaError(Exception):
    def __init__(self, messagem:str):
        super().__init__(messagem)

class No:
    def __init__(self,carga):
        self.carga = carga
        self.proximo = None

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

    def busca(self,valor):
        assert not self.vazia(), 'lista vazia'
        cursor = self.__head.inicio
        contador = 1
        while cursor is not None:
            if cursor.carga == valor:
                return cursor.carga
            cursor = cursor.proximo
            contador += 1
        raise KeyError('N existe esse valor')
    
    def elemento(self,posicao):
        """retorna a carga armazenada na posição
           especificada como argumento"""
        assert posicao>0  and posicao<len(self), 'posicao fora do range'
        assert not self.vazia(),'lista vazia'
        cursor = self.__head.inicio
        #while cursor is note None and posicao>0:
        for i in range(posicao-1):
            cursor = cursor.proximo
        
        return cursor.carga
            
    def inserir(self,posicao,carga):
        # CONDICAO 1: insercao se a lista estiver vazia
        #assert posicao>0 and posicao<=len(self)+1,'posicao nao encontrada'
        if self.vazia():
            if posicao != 1:
                raise ListaError('lista vazia, tem que inserir na 1 posicao obrigatorio')
            novo = No(carga)
            self.__head.inicio = self.__head.fim = novo
            self.__head.tamanho += 1
            return
        # CONDICAO 2: insercao na primeira posicao em uma lista nao vazia
        if posicao == 1:
            novo = No(carga)
            novo.proximo = self.__head.inicio
            self.__head.inicio = novo
            self.__head.tamanho += 1
            return

        # CONDICAO 3: insercao apos a primeira posicao em lista nao vazia
        contador = 1
        cursor = self.__head.inicio
        #ele ta checando aqui para as posiçoes do meio
        #da lista, sera criada uma condiçao para a ultima posicao
        while contador < (posicao-1):
            cursor = cursor.proximo
            contador +=1
        
        novo = No(carga)
        novo.proximo = cursor.proximo
        cursor.proximo = novo
            
        if posicao == (len(self)+1):
            self.__head.tail = novo

        self.__head.tamanho += 1

    def remover(self,posicao):
        
        assert not self.vazia(),'lista vazia para remoçao'
        
        if posicao<0 or posicao>len(self):
            raise ListaError ('digite uma posicao valida')
        
        cursor = self.__head.inicio
        
        for i in range(posicao):
            anterior = cursor
            cursor = cursor.proximo
            
        if( posicao == 0):
            self.__head.inicio = cursor.proximo
            
        else:
            anterior.proximo = cursor.proximo
            
        if posicao == len(self)-1:
            self.__head.fim = anterior
        self.__head.tamanho -= 1   

    def merge(self,lista):
        """combina duas listas, retorna uma nova lista"""
        combinaçao = Lista()
        cursor = self.__head.inicio
        i = 1
        while cursor is not None:
            combinaçao.inserir(i,cursor.carga)
            i+=1
            cursor = cursor.proximo 
        cursor = lista.__head.inicio
        j = 1
        while cursor is not None:
            combinaçao.inserir(j,cursor.carga)
            j+=1
            cursor = cursor.proximo
        return combinaçao


    def modificar(self,posicao,carga):
        assert not posicao > 0 and posicao <= len(self),'diga uma posicao valida'
        assert not self.vazia()
        cursor = self.__head.inicio
        contador = 1
        while (contador < posicao): #duvida: pq tem que pecorrer ate -1? se vai mudar a carga
            cursor = cursor.proximo   #exata da POSICAO pq ficar atras ? ou pq nao fazer
            contador += 1                                                # cursor.proximo.carga = carga

        cursor.carga = carga
        return

    def __str__(self):
        s = '['
        cursor = self.__head.inicio
        while(cursor):
            s += f'{cursor.carga}, '
            cursor = cursor.proximo
        s = s.rstrip(', ')
        s += ' ]'
        return s


lista1 = Lista()
lista2 = Lista()

lista1.inserir(1, "A")
lista1.inserir(2, "B")

lista2.inserir(1, "C")
lista2.inserir(2, "D")

combinada = lista2.merge(lista1)
print(combinada)  # Esperado: [A, B, C, D]



   # def append(self,elem):
    #     """  insere elementos
    #      no fim da lista, replicando o append
    #        """
    #     if self.__head.inicio is not None:#se tiverem elementos ja na lista
    #         cursor = self.__head.inicio
    #         #percorrendo ate o ponteiro n ter mais proximo(no caso, qnd ele for None)
    #         while(cursor.prox):
    #             cursor = cursor.prox
    #         #qnd o while acaba, o ponteiro n tem mais proximo
    #         #portanto, essa linha muda o None para No(elem) [que seria o novo ultimo no]
    #         cursor.prox = No(elem)
            
    #     else:
    #         #primeiro elemento
    #         self.__head.inicio = No(elem)
    #     self.__head.tamanho+=1