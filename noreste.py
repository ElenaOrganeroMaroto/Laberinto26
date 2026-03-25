class Noreste:
    _unica_instancia = None

    @classmethod
    def default(cls):
        if cls._unica_instancia is None:
            cls._unica_instancia = super(Noreste, cls).__new__(cls)
        return cls._unica_instancia

    def __init__(self):
        if Noreste._unica_instancia is not None:
            raise Exception("No se puede crear objeto")

    def caminar(self, unBicho):
        elemento_mapa = unBicho.posicion.forma.ne
        elemento_mapa.entrar(unBicho)

    def ponerElemento_enContenedor(self, unEM, unCont):
        unCont.ne = unEM

    def recorrer_enContenedor(self, unBloque, unCont):
        unCont.ne.recorrer(unBloque)