from laberinto_builder import LaberintoBuilder
from rombo import Rombo

class LaberintoBuilderRombo(LaberintoBuilder):
    def __init__(self):
        super().__init__()

    def asignarOrientaciones(self, unaForma):
        unaForma.orientaciones.append(self.fabricarNoreste())
        unaForma.orientaciones.append(self.fabricarNoroeste())
        unaForma.orientaciones.append(self.fabricarSureste())
        unaForma.orientaciones.append(self.fabricarSuroeste())

    def fabricarForma(self):
        forma = Rombo()        
        self.asignarOrientaciones(forma)
        return forma