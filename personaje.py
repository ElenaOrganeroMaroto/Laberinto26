from ente import Ente

class Personaje(Ente):
    def __init__(self, nombre="Prota"):
        super().__init__()
        self.nombre = nombre

    def buscarEnemigo(self):
        return self.juego.obtenerBichoEn(self.posicion)

    def irA(self, unaOr):
        unaOr.caminar(self)

    def irAlNorte(self):
        self.posicion.irAlNorte(self)

    def muero(self):
        self.juego.muerePersonaje()

    def __str__(self):
        return str(self.nombre)