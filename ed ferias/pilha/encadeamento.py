# O que a gente quer guardar no nó
# Qual é o próximo nó

class No:
    def __init__(self, carga):
        self.carga = carga
        self.proximo = None


no1 = No(5)
no2 = No(9)
no3 = No(10)

no1.proximo = no2
no2.proximo = no3