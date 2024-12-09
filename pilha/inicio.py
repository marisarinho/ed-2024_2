class PilhaSequencial:
    def __init__(self):
        self.__dados = []
    def isempty(self):
        vazio = False
        if len(self.__dados)==0:
            vazio = True
        return vazio
    def tamanho(self):
        return len(self.__dados)
    def topo(self):
        return self.__dados[0]
    def inserir(self,dado):
        self.__dados.append(dado)