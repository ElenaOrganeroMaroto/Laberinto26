class Modo:
    def __init__(self):
        pass

    def actua(self, unBicho):
        self.camina(unBicho)
        self.ataca(unBicho)
        self.duerme(unBicho)

    def ataca(self, unBicho):
        unBicho.atacar()

    def camina(self, unBicho):
        orientacion = unBicho.obtenerOrientacionAleatoria()        
        orientacion.caminar(unBicho)

    def duerme(self, unBicho):
        pass
    
    def esAgresivo(self):
        return False

    def esPerezoso(self):
        return False