class Carta:
    def __init__(self,valor,naipe):
        self.__valor = valor
        self.__naipe = naipe
    
    def __str__(self):
        return(f'{self.__valor} de {self.__naipe}')

    def get_valor(self):
        return self.__valor
    
    def get_naipe(self)->str:
        return self.__naipe
    