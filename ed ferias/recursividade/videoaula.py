# str = 'ifpb'
# for i in str:
#     print(i)
# como fazer o algoritmo acima se recursivo??

def printstr(str):
    if (str == ''):
        return
    print(str[0], end='')
    printstr(str[1:]) #como ja passou o 1(o 0 no caso), segue a partir do 1 em diante


def printInvertida(str):
    if (str == ''):
        return
    printInvertida(str[1:])
    print(str[0], end='')
    #quando a acao vem dps da chamada recursiva, ela funciona meio que como uma pilha
    #fica invertida

def tamanhostr(str):
    if (str == ''):
        return 0
    else:
        return 1 + tamanhostr(str[1:])
    
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)




str = 'ifpb'
printstr(str)
print(' ')
printInvertida(str)
print(' ')
print('tamanho:',tamanhostr(str))