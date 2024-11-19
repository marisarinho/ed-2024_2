
class Jogador:
    def __init__(self,nome):
        self.nome = nome
        self.__cartas = []

    def comprar_carta(self,carta):
        self.__cartas.append(carta)

    def mostrar_cartas(self):
        for i, carta in enumerate(self.__cartas):
            #.__str__ depois da carta pq, por exemplo:
            #o obj carta tem seu proprio metodo str
            #(nao vai aceitar essa formataçao se nao chamar o str dela)
            print(f'{carta.__str__():20}')
            if i == len(self.__cartas):
                print()
    