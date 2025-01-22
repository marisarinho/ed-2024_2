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
        assert posicao>0 and posicao<=len(self)+1,'posicao nao encontrada'
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

    

    def modificar(self,posicao,carga):
        assert posicao > 0 and posicao <= len(self),'diga uma posicao valida'
        assert not self.vazia()
        cursor = self.__head.inicio
        contador = 1
        while (contador < posicao): #duvida: pq tem que pecorrer ate -1? se vai mudar a carga
            cursor = cursor.proximo   #exata da POSICAO pq ficar atras ? ou pq nao fazer
            contador += 1                                                # cursor.proximo.carga = carga

        cursor.carga = carga
        return


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



    def __str__(self):
        s = '['
        cursor = self.__head.inicio
        while(cursor):
            s += f'{cursor.carga}, '
            cursor = cursor.proximo
        s = s.rstrip(', ')
        s += ' ]'
        return s
        
# Criando uma instância da lista encadeada
lista = Lista()

# Inserindo elementos para testes
lista.inserir(1, 10)  # Inserindo na posição 1
lista.inserir(2, 20)  # Inserindo na posição 2
lista.inserir(3, 30)  # Inserindo na posição 3
lista.inserir(4, 40)  # Inserindo na posição 4

print("Lista original:")
print(lista)  # Esperado: [10, 20, 30, 40]

# Caso 1: Modificar o primeiro elemento
lista.modificar(1, 99)
print("Após modificar a posição 1 para 99:")
print(lista)  # Esperado: [99, 20, 30, 40]

# Caso 2: Modificar um elemento do meio da lista
lista.modificar(3, 77)
print("Após modificar a posição 3 para 77:")
print(lista)  # Esperado: [99, 20, 77, 40]

# Caso 3: Modificar o último elemento
lista.modificar(4, 55)
print("Após modificar a posição 4 para 55:")
print(lista)  # Esperado: [99, 20, 77, 55]
