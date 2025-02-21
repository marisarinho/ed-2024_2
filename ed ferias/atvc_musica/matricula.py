from BinarySearchTree import BinarySearchTree

class ColetorDeMatricula:
    def __init__(self):
        self.matriculas = BinarySearchTree()

    def efetuar_matricula(self, candidato:Candidato):
        ' ' ' Permite a duplicidade de matrículas ' ' '
        self.matriculas.add(candidato)

    def __len__(self):
        return len(self.matriculas)

    def pesquisar_candidato(self,chave:Candidato)->Candidato:
        return self.matriculas.search(chave)


    def eliminar_duplicatas(self):
        assert not self.matriculas.isEmpty(), "arvore vazia"
        valores = []
        self.matriculas.__preorder()

    def exibir_resultado(self):
        '''
        Exibe a lista dos candidatos aprovados, em ordem alfabética.
        '''
        self.percorrer_em_ordem(self.__root)

    def em_ordem(self, node):
        if node:
            self.em_ordem(node.left) 
            print(node.data)  
            self.ordem(node.right) 

