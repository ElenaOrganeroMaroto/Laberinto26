from contenedor import Contenedor

class Habitacion(Contenedor):
    def __init__(self, num):
        super().__init__()
        self.num = num  
    
    def entrar(self, alguien):
        print(f"Estas en la habitacion {self.num}")

    
    def recorrer(self, func):
        print(f"Habitacion-{self.num}")

        func(self)  # unBloque value: self
        for hijo in self.hijos:  
            hijo.recorrer(func)
    
    def __str__(self):
        return f"Habitación {self.num}"