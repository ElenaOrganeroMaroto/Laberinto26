
class Bicho:
    def __init__(self, vidas: int, poder: int, modo, posicion=None):
        self.vidas: int = vidas
        self.poder: int = poder
        self.modo = modo
        self.posicion = posicion
    
    def actua(self):
        if self.modo:
            self.modo.actua(self) #Cada bicho actuará según su modo
    
    def __str__(self):
        return f"Bicho (vidas: {self.vidas}, poder: {self.poder})"