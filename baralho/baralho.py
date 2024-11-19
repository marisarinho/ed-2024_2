import random
from cartas import Carta

class Baralho:

    valores = ["2" , "3" , "4" , "5" , "6" , "7" , "8" ,"9" , "10" , "Valete", "Dama", "Rei", "Ás"]
    naipes = ["Paus", "Ouros", "Copas", "Espadas"]

    def __init__(self):
        self.cartas = []
        baralho = []
        for valor in self.valores:
            for naipe in self.naipes:
                c = Carta(valor,naipe)
                self.cartas.append(c)  

    def __len__(self):
        return len(self.cartas)

    def __str__(self):
        string_final = ''
        for i, carta in enumerate(self.cartas):
            substring = f'{carta.__str__():20} '
            if (i+1) % 4 == 0:
                substring += '\n'
            string_final += substring
        return string_final
    
    def embaralhar(self):
        return random.shuffle(self.cartas)
    
    def remover_carta(self):
        return self.cartas.pop()
    
    def removerVariasCartas(self,num_cartas):
        for _ in range(num_cartas):
            self.remover_carta()
    
    

#print(Baralho())
#baralho = Baralho()
#baralho.printar_cartas()
#ultimaCarta = baralho.remover_carta()
#print(ultimaCarta)