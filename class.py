class Calculadora:
    def __init__(self, marca:str, valor1:float,valor2:float):
        self.marca = marca
        self.valor1 = valor1
        self.valor2 = valor2

    def soma(self) -> float:
        return self.valor1 + self.valor2
    
    def sub(self) -> float:
        return self.valor1 - self.valor2
    
    def vezes(self) -> float:
        return self.valor1 * self.valor2
    
    def divisao(self) -> float:
        return self.valor1 / self.valor2
    


casio = Calculadora(marca='casio',valor1=23,valor2=45)
hp = Calculadora(marca='hp',valor1=10,valor2=20)

print(casio.soma())
print(hp.divisao())