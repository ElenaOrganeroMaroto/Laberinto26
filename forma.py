import random

class Forma:
    def __init__(self):
        self.orientaciones = [] 
        self.num = None

    def agregarOrientacion(self, unaOr):
        self.orientaciones.append(unaOr)

    def eliminarOrientacion(self, unaOr):
        self.orientaciones.remove(unaOr)

    def obtenerOrientacionAleatoria(self):
        limite = len(self.orientaciones)
        ind = random.randint(0, limite - 1)
        return self.orientaciones[ind]

    def ponerEn_elemento(self, unaOr, unEM):
        unaOr.ponerElemento_enContenedor(unEM, self)

