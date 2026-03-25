from contenedor import Contenedor

class Laberinto(Contenedor):
    def __init__(self):
        super().__init__() 

    def agregarHabitacion(self, unaHab):
        self.agregarHijo(unaHab)

    def entrar(self, alguien):
        print(alguien, " ha entrado en el laberinto")        
        hab = self.obtenerHabitacion(1)        
        if hab:
            hab.entrar(alguien)

    def obtenerHabitacion(self, unNum):
        for each in self.hijos:
            if each.num == unNum:
                return each
        return None

    def recorrer(self, unBloque):
        print("Recorriendo el laberinto")        
        for each in self.hijos:
            each.recorrer(unBloque)