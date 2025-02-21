class No:
    def __init__(self, carga):
        self.esq = self.dir = None
        self.carga = carga
    
    def __str__(self):
        return str(self.carga)