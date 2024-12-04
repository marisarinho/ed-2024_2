class PilhaError(Exception):
    def __init__(self, messagem:str):
        super().__init__(messagem)


class No:
    def __init__(self, carga:any):
        self.carga = carga
        self.prox = None

    def __str__(self):
        return f'{self.carga}'

class Pilha:
    def __init__(self):
        self.__head = None # o head é o "topo"
        self.__tamanho = 0


    def vazia(self):
        '''
        Retorna True se a pilha estiver vazia,
        caso contrario, False
        '''
        return self.__head == None
    
    def topo(self)->any:
        '''Retona o conteúdo que está no topo da pilha, 
           sem removê-lo.'''
        if self.vazia():
            raise PilhaError('Não há topo porque a pilha está vazia')
        else:
            return self.__head.carga
    
    def pesquisa(self, key:any)->any:
        '''
        Localiza a carga na pilha correspondente à chave passada como argumento.
        Se a chave não for encontrada, lança um KeyError
        '''
        cursor = self.__head
        while(cursor is not None):
            if cursor.carga == key:
                return cursor.carga
            cursor = cursor.prox
        raise KeyError(f'Chave {key} não encontrada na pilha')

    def elemento(self, posicao:int)->any:
        '''
        Retorna a carga armazenada na posição especificada como argumento.
        Se a posição não existir, lança um PilhaError
        '''
        if posicao < 0 or posicao > len(self):
            raise PilhaError(f'Posição {posicao} fora dos limites da pilha')
        cursor = self.__head
        for i in range(len(self), posicao, -1):
            cursor = cursor.prox
        return cursor.carga

    def empilha(self, carga:any):
        '''
        Adiciona um novo elemento no topo da pilha
        ''' 
        
        novo = No(carga)
        novo.prox = self.__head
        self.__head = novo
        self.__tamanho += 1
    
    def desempilha(self)->any:
        '''
        Remove o conteúdo que está no topo da pilha e retorna-o.
        Lança um PilhaError se a pilha estiver vazia 
        '''
        if self.vazia():
            raise PilhaError('Pilha vazia. Não é possível remover elementos')
        else:
            carga = self.topo()
            self.__head = self.__head.prox
            self.__tamanho -= 1
            return carga

    def __len__(self):
        return self.__tamanho
    
    def __str__(self):
        s = 'topo->['
        cursor = self.__head
        while(cursor):
            s += f'{cursor.carga}, '
            cursor = cursor.prox
        s = s.rstrip(', ')
        s += ' ]'
        return s