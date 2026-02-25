from contenedor import Contenedor

class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()
    
    def agregar_habitacion(self, unaHab):
        self.agregar_hijo(unaHab)
    
    def obtener_habitacion(self, unNum):
        for habitacion in self.hijos:
            if habitacion.num == unNum:
                return habitacion
        return None
    
    def recorrer(self, func):
        print("Recorriendo el laberinto")
        for habitacion in self.hijos:
            habitacion.recorrer(func)
    
    def entrar(self, alguien):
        if self.hijos:
            return self.hijos[0].entrar(alguien) #Si hay habitaciones entra en la primera
        return None
    
    def __str__(self):
        return f"Laberinto con {len(self.hijos)} habitaciones"