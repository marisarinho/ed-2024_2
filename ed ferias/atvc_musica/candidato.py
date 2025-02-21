class Candidato:
    def __init__(self, rg:int, nome:str, instrumento:str):
        self.rg = rg
        self.nome = nome
        self.instrumento = instrumento
    def __str__(self):        
        return f"RG: {self.rg}, Nome: {self.nome}, Instrumento: {self.instrumento}"
    
    def __lt__(self, outro): # <
        return self.rg < outro.rg

    def __gt__(self, outro): # >
        return self.rg > outro.rg
    
    def __eq__(self, outro): # ==
        return self.rg == outro.rg
