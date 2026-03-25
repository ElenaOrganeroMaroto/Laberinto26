class Oeste:
    _unica_instancia = None

    @classmethod
    def default(cls):
        if cls._unica_instancia is None:
            cls._unica_instancia = super(Oeste, cls).__new__(cls)
        return cls._unica_instancia

    def __init__(self):
        if Oeste._unica_instancia is not None:
            raise Exception("No se puede crear objeto")

    def caminar(self, unBicho):
        elemento_mapa = unBicho.posicion.forma.oeste
        elemento_mapa.entrar(unBicho)

    def ponerElemento_enContenedor(self, unEM, unCont):
        unCont.oeste = unEM

    def recorrer_enContenedor(self, unBloque, unCont):
        unCont.oeste.recorrer(unBloque)