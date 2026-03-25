from juego import Juego
from pared_bomba import ParedBomba

class JuegoBombas(Juego):

    def fabricarPared(self):
        return ParedBomba()