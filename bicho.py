from ente import Ente

class Bicho(Ente):
    def __init__(self, modo=None):
        super().__init__()
        self.modo = modo

    def actua(self):
        self.modo.actua(self)

    def buscarEnemigo(self):
        return self.juego.buscarPersonaje(self)

    def esAgresivo(self) -> bool:
        return self.modo.esAgresivo()

    def esPerezoso(self) -> bool:
        return self.modo.esPerezoso()

    def muero(self):
        self.juego.muereBicho(self)

    def obtenerOrientacionAleatoria(self):
        return self.posicion.obtenerOrientacionAleatoria()

    def __str__(self):
        return f"Bicho-{self.modo}"