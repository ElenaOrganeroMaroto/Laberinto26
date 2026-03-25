from elemento_mapa import ElementoMapa

class Hoja(ElementoMapa):
    def __init__(self):
        super().__init__()

    def recorrer(self, unBloque):
        print(self) 
        unBloque(self)

    def entrar(self, alguien):
        #Este método es obligatorio porque ElementoMapa lo pide,        """
        pass

  