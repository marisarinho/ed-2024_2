class ListaError(Exception):
    def __init__(self, messagem:str):
        super().__init__(messagem)


class No:
    def __init__(self, carga:any):
        self.carga = carga
        self.prox = None

    def __str__(self):
        return f'{self.carga}'


class Controle:
    def __init__(self):
        self.head = None
        self.tail = None
        self.tamanho = 0


class Lista:
    def __init__(self):
        self.__head = Controle()


    def vazia(self):
        return self.__head.head == None
        # return self.__head.tamanho == 0
    
    
    def pesquisa(self, key:any)->any:
        '''
        Localiza a carga na fila correspondente à chave passada como argumento.
        Se a chave não for encontrada, lança um KeyError
        '''
        cursor = self.__head.head
        while(cursor is not None):
            if cursor.carga == key:
                return cursor.carga
            cursor = cursor.prox
        raise KeyError(f'Chave {key} não encontrada na pilha')

    def get(self, posicao:int)->any:
        '''
        Retorna a carga armazenada na posição especificada como argumento.
        Se a posição não existir, lança um FilaError
        '''
        if posicao < 0 or posicao > len(self):
            raise ListaError(f'Posição {posicao} fora dos limites da lista')
        cursor = self.__head.head
        # for i in range(1,posicao):    
        for i in range(posicao-1):
            cursor = cursor.prox
        return cursor.carga

    def inserir(self, posicao:int,  carga:any):
        try:
            assert posicao > 0 and posicao <= len(self)+1, f'Posicao invalida. Lista contém {self.__tamanho} elementos' 

            # CONDICAO 1: insercao se a lista estiver vazia
            if (self.vazia()):
                if ( posicao != 1):
                    raise ListaError(f'A lista esta vazia. A posicao correta para insercao é 1.')

                self.__head.head = self.__head.tail = No(carga)
                self.__head.tamanho += 1
                return
            
            # CONDICAO 2: insercao na primeira posicao em uma lista nao vazia
            if ( posicao == 1):
                novo = No(carga)
                novo.prox = self.__head.head
                self.__head.head = novo
                self.__head.tamanho += 1
                return

            # CONDICAO 3: insercao apos a primeira posicao em lista nao vazia
            cursor = self.__head.head
            contador = 1
            while ( contador < posicao-1):
                cursor = cursor.prox
                contador += 1

            novo = No(carga)
            novo.prox = cursor.prox
            cursor.prox = novo

            if posicao == len(self)+1:
                self.__head.tail = novo

            self.__head.tamanho += 1

        except TypeError:
            raise ListaError(f'A posição deve ser um número inteiro')            
        except AssertionError:
            raise ListaError(f'A posicao não pode ser um número negativo ou 0 (zero)')
    
    def append(self, carga:any):
        self.inserir(len(self)+1, carga)
        # novo = No(carga)
        # if self.estaVazia():
        #     self.__head.head = self.__head.tail = novo
        # else:
        #     self.__head.tail.prox = novo
        #     self.__head.tail = novo
        # self.__head.tamanho += 1

    
    def remover(self, posicao:int)->any:
        '''
        Remove o conteúdo que está na frente da fila e retorna-o.
        Lança um FilaError se a fila estiver vazia
        '''
        try:
            if( self.vazia() ):
                raise ListaError(f'Não é possível remover de uma lista vazia')
            
            assert posicao > 0 and posicao <= len(self), f'Posicao invalida. Lista contém {self.__tamanho} elementos'

            cursor = self.__head.head
            contador = 1

            while( contador <= posicao-1 ) :
                anterior = cursor
                cursor = cursor.prox
                contador+=1

            carga = cursor.carga

            if( posicao == 1):
                self.__head.head = cursor.prox
            else:
                anterior.prox = cursor.prox
                
            if posicao == len(self):
                self.__head.tail = anterior

            self.__head.tamanho -= 1
            return carga
        
        except TypeError:
            raise ListaError(f'A posição deve ser um número inteiro')            
        except AssertionError:
            raise ListaError(f'A posicao não pode ser um número negativo')

    def __len__(self):
        return self.__head.tamanho
    
    def __str__(self):
        s = '['
        cursor = self.__head.head
        while(cursor):
            s += f'{cursor.carga}, '
            cursor = cursor.prox
        s = s.rstrip(', ')
        s += ' ]'
        return s
        


    
        
