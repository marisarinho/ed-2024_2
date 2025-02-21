from BinarySearchTree import BinarySearchTree
from candidato import Candidato

arv = BinarySearchTree()

arv.add(Candidato(123,'Maria Clara', 'guitarra'))
arv.add(Candidato(456,'Mariana', 'flauta transversal'))
arv.add(Candidato(777,'Zenildo', 'Acordeon'))
arv.add(Candidato(123,'Maria Clara', 'bateria'))
arv.add(Candidato(123,'Maria Clara', 'contrabaixo'))
arv.add(Candidato(888,'Alex', 'piano'))

# print(len(arv))
# key = Candidato(999,'','')
# print(arv.search( key ))


print(arv.search(123))