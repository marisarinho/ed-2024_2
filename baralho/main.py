import random

class Carta:
    def __init__(self,valor,naipe):
        self.__valor = valor
        self.__naipe = naipe

    def get_valor(self):
        return self.__valor
    
    def get_naipe(self)->str:
        return self.__naipe
    
    def __str__(self):
        return(f'{self.__valor} de {self.__naipe}')


class Baralho:

    valores = ["2" , "3" , "4" , "5" , "6" , "7" , "8" ,"9" , "10" , "Valete", "Dama", "Rei", "Ás"]
    naipes = ["Paus", "Ouros", "Copas", "Espadas"]

    def __init__(self):
        self.cartas = []
        baralho = []
        for valor in self.valores:
            for naipe in self.naipes:
                carta = (f'{valor} de {naipe}')
                self.cartas.append(carta)     

    def printar_cartas(self):
        for i, carta in enumerate(self.cartas):
            print(f'{carta:20}', end=' ')
            if (i+1) % 4 == 0:
                print()
    
    def embaralhar(self):
        return random.shuffle(self.cartas)
    
   # def distribuir(self):