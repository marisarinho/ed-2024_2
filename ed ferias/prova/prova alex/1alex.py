"""Considere a implementação de uma Fila Encadeada com nó cabeça vista em sala de aula. Surgiu a
necessidade de adicionar uma nova operação na Fila que remova todos os seus elementos (esvaziar)
desde que a soma das cargas de todos os elementos não atinja o limiar estabelecido por parâmetro.
O retorno do método indica se houve sucesso ou falha na tentativa de esvaziamento. A codificação
deve ser realizada utilizando a técnica encadeada. A estrutura das classes é ilustrada adiante."""

"""class Node:
def __init__(self, carga:any):
self.carga = carga
self.prox = None

class Head:
def __init__(self):
self.inicio = None
self.fim = None
self.tamanho = 0

class Fila:
def __init__(self):
self.head = Head()

Operações que podem ser utilizadas no suporte à implementação: estaVazia(), busca(),
__len__(), __str__()

def esvazia ( self, limiar:float )->bool:
    pass
"""
def esvazia(self,limiar):
    soma = 0
    cursor = self.head.inicio
    while cursor is not None:
        soma += cursor.carga
        cursor = cursor.proximo
    if soma < limiar:
        self.head.inicio = None
        self.tamanho = 0
        self.head.fim = None
        return True
    else:
        return False
