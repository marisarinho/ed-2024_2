class No:
    def __init__(self,carga):
        self.carga = carga
        self.proximo = None
    def __str__(self):
        return f'{self.carga}'

class Controle:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

class Fila:
    def __init__(self):
        self.__head = Controle()

    def __len__(self):
        return self.__head.tamanho
    
    def vazia(self):
        return self.__head.inicio == None
    
    def esvaziar(self):
        self.__tamanho = 0
        self.__head.inicio = None
    
    def elemento_da_frente(self):
        """retorna o 1 elemento da fila sem remove-lo"""
        assert not self.vazia(), 'fila vazia'
        return self.__head.inicio.carga
    
    def elemento(self,posicao):
        """retorna a carga armazenada na posição
           especificada como argumento"""
        assert not posicao<0 or posicao>(len(self)), 'posicao nao existente'
        cursor = self.__head.inicio
        for i in range(posicao-1):
            cursor = cursor.prox
        return cursor.carga
    
    def pesquisa(self,chave):
        """ localiza a carga na fila correspondente
        à chave passada como argumento."""
        cursor = self.__head.inicio
        while(cursor is not None):
            if cursor.carga == chave:
                return cursor.carga
            cursor = cursor.prox
        raise KeyError('chave nao encontrada')
    
    def enfileira(self,carga):
        """
        enfileira normal por ordem de chegada"""
        novo = No(carga)
        if self.vazia():
            self.__head.inicio = self.__head.fim = novo
        else:
            self.__head.fim.proximo = novo
            self.__head.fim = novo
        
        self.__head.tamanho += 1

    def desenfileira(self):
        """
        remove o 1 elemento e retorna ele
        """
        assert not self.vazia(), 'fila vazia'
        carga = self.elemento_da_frente()
        if (len(self)==1):
            self.__head.inicio = self.__head.fim = None
        else:
            self.__head.inicio = self.__head.inicio.proximo

        self.__head.tamanho -= 1
        return carga
    
    def copia(self):
        """faz uma copia e a retorna"""
        copia= Fila()
        cursor = self.__head.inicio
        while cursor is not None:
            copia.enfileira(cursor.carga)
            cursor = cursor.proximo
        return copia

    def copia_invertida(self):
        """retorna uma copia invertida"""
        # copia = Fila()
        # for i in range(len(self)):
        #     copia.enfileira(self.desenfileira())
        # return copia

#abaixo codigo do chatgpt
        # copia = Fila()
        # aux = Fila()

        # # Copiar os elementos da fila original para a fila auxiliar sem modificar a original
        # cursor = self.__head.inicio
        # while cursor is not None:
        #     aux.enfileira(cursor.carga)
        #     cursor = cursor.proximo
        
        # # Agora, desenfileiramos da fila auxiliar e inserimos na cópia, o que inverte a ordem
        # while not aux.vazia():
        #     carga = aux.desenfileira()  # Desenfileira o primeiro item da fila auxiliar
        #     copia.enfileira(carga)  # Enfileira na cópia, invertendo a ordem dos elementos

        # return copia




    def inverter(self):
        """inverte a fila original"""
        # aux = self.copia_invertida()
        # aux2 = Fila()
        # while not aux.vazia():
        #     aux2.enfileira(aux.desenfileira())
        # while not aux2.vazia():
        #     self.enfileira(aux2.desenfileira())


        # copia = self.copia()
        # self.esvaziar()
        # cursor = self.__head.inicio
        # while cursor is not None:
        #     self.enfileira(cursor.carga)
        #     cursor = cursor.proximo

        aux= Fila()
        while not self.vazia():
            aux.enfileira(self.desenfileira())
        while not aux.vazia():
            self.enfileira(aux.desenfileira())

            
    def __str__(self):
        s = 'frente->['
        cursor = self.__head.inicio
        while(cursor):
            s += f'{cursor.carga}, '
            cursor = cursor.proximo
        s = s.rstrip(', ')
        s += ' ]<-fim'
        return s
        
fila = Fila()
fila.enfileira(1)
fila.enfileira(2)
fila.enfileira(3)
invertida = fila.inverter()
print(fila)
print(invertida)
    