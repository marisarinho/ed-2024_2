
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
        assert not posicao<0 and posicao>(len(self)), 'posicao nao existente'
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
        pilha = []
        copia = Fila()
        cursor = self.__head.inicio
        while cursor is not None:
            pilha.append(cursor.carga)
            cursor = cursor.proximo
        while len(pilha)>0:
            copia.enfileira(pilha.pop())
        return copia
        
    
        # copia = Fila()
        # for i in range(len(self)):
        #     copia.enfileira(self.desenfileira())
        # return copia

    def inverter(self):
        pilha = []
        while not self.vazia():
            pilha.append(self.desenfileira())
        while pilha: 
            self.enfileira(pilha.pop())
            

    def __str__(self):
        s = "" 
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
print("Fila original:", fila)
fila.copia_invertida()
print("Fila invertida:", fila)

fila = Fila()
fila.enfileira(1)
fila.enfileira(2)
fila.enfileira(3)

fila_invertida = fila.copia_invertida()

print("Fila original:", fila)  # Deve mostrar na ordem: 1, 2, 3
print("Fila invertida:", fila_invertida)  # Deve mostrar na ordem: 3, 2, 1
