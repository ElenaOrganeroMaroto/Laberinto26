class Orientacion:
    def __init__(self):
        pass

    def caminar(self, unBicho):
        raise NotImplementedError("Debe ser implementado por la subclase")

    def ponerElemento_enContenedor(self, unEM, unCont):
        raise NotImplementedError("Debe ser implementado por la subclase")

    def recorrer_enContenedor(self, unBloque, unCont):
        raise NotImplementedError("Debe ser implementado por la subclase")