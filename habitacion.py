from contenedor import Contenedor

class Habitacion(Contenedor):
    def __init__(self, num=None):
        super().__init__()
        self.num = num  
    
    def entrar(self, alguien):
        print(f"Estas en la habitacion {self.num}")

