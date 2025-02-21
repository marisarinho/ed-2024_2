# def print_lista_ordem_inversa(self, no):
#     if no is None:
#         return
#     else:
#         print_lista_ordem_inversa(no.next)
#         print(no.carga)


def fib(n)->int:
    return n if n==0 or n==1 else fib(n-1) + fib(n-2)
    # if n == 0 or n == 1:
    #     return n
    # else:
    #     return fib(n-1) + fib(n-2)                        


def sequencia_iterativa(inicial, final):
    for i in range(inicial, final+1):
        print(i, end=' ')

def sequencia_recursiva(inicial, final):
    if inicial > final:
        return

    sequencia_recursiva(inicial+1,final)
    print(inicial, end=' ')

def print_str(string):
    if len(string) == 0:
        return

    print(string[0],end='')
    print_str(string[1:])

def contar_caracteres(string)->int:
    if len(string)==0:
        return 0
    else:
        return 1 + contar_caracteres(string[1:])
    

def invictus

sequencia_iterativa(2,10)
print()
sequencia_recursiva(5,11)
print()
print(fib(7))
print_str("estrutura de dados")
print()
print(contar_caracteres("ifpb sistemas"))