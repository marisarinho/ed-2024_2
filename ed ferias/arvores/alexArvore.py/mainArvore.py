from AvoreBinaria import ArvoreBinaria
from no import No

arvore = ArvoreBinaria(10)

print(arvore.get_cursor())
print(len(arvore))

arvore.add_dir(6)
arvore.desce_direita()
print(arvore.get_cursor())
arvore.add_esq(7)
arvore.add_dir(8)
raiz = arvore.get_raiz()
print(arvore.get_cursor())
print(len(arvore))

# quebra encapsulamento
input()
arvore.pre_ordem()
len(arvore)
no_bagunca = No('no impostor')
raiz.dir = no_bagunca
arvore.pre_ordem()
len(arvore)
input()


arvore.desce_direita()
arvore.add_dir(9)
print(arvore.get_raiz())
print(arvore.get_cursor())
print(len(arvore))

arvore.pre_ordem()
print()
arvore.em_ordem()
print()
arvore.pos_ordem()
