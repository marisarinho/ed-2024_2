import time
from baralho import Baralho
from jogador import Jogador

class Jogo:
    def __init__(self, jogadores: list[Jogador]):
        self.baralho = Baralho()
        self.jogadores = jogadores

    def distribuir(self):
        qtd_cartas_baralho = len(self.baralho)
        qtd_jogadores = len(self.jogadores)
        qtd_cartas_por_jogador = qtd_cartas_baralho // qtd_jogadores 
        resto = qtd_cartas_baralho % qtd_jogadores
        for _ in range(qtd_cartas_por_jogador):
            #entregando as cartas uma por vez
            for j in range(qtd_jogadores):
                carta = self.baralho.remover_carta()
                self.jogadores[j].comprar_carta(carta)    
        print(resto)

    def mostrartodascartas(self):
        for i in range(len(self.jogadores)):
            self.jogadores[i].mostrar_cartas()
            print()

    def cartasQueSobraram(self):
        print(f'\ncartas {self.baralho}')


mari = Jogador('mari')
ana = Jogador('ana')
davi = Jogador('davi')
dc = Jogador('dc')
dce = Jogador('dce')
jogadores = [mari, ana, davi, dc, dce]
jogo = Jogo(jogadores)
jogo.distribuir()
#jogo.mostrartodascartas()
print(mari.nome)
mari.mostrar_cartas()
print(ana.nome)
ana.mostrar_cartas()
print (davi.nome)
davi.mostrar_cartas()
print(dc.nome)
dc.mostrar_cartas()
print(dce.nome)
dce.mostrar_cartas()
jogo.cartasQueSobraram()
