"""Codifique a função reverseWords() conforme protótipo definido a seguir. A função recebe o
argumento frase que pode ser constituída por diversas palavras. Então, a função deve fazer uso
apenas da estrutura de dados pilha para realizar o trabalho de inversão das palavras. O retorno da
função é um string com o resultado das palavras invertidas. ............. (2,5 pontos)

from Pilha import Pilha

def reverseWords(frase:str)->str:
    pass
Exemplo de uso
novaFrase = reverseWords('Fila e Pilha encadeada ')
print(novaFrase)
# Saída:
# aliF e ahliP adaedacne
# """

def inverter(self):
    cursor = self.topo
    self.esvaziar()
    while cursor is not None:
        self.empilha(cursor.carga)
        cursor = cursor.proximo

def reverse(frase):
    pilha = Pilha()
    invertida = ''
    for i in frase:
        pilha.empilha(i)
    while not pilha.estaVazia():
        invertida += pilha.desempilha()
    return invertida
