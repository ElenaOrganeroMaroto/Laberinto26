from decorator import Decorator

class Bomba(Decorator):
    def __init__(self, em):
        super().__init__(em, "Bomba")  # Se le pasa el nombre que se le asigna a la hoja
        self.activa = False

    def activar(self):
        self.activa = True

    def desactivar(self):
        self.activa = False

    def entrar(self, alguien):
        if self.activa:
            print("¡BOOM! Has chocado con una bomba")
            # Aquí se puede poner si se quita vida, etc.
            # self.activa = False  # ¿Se desactiva al explotar?
        return self.em.entrar(alguien)   # Delegar al elemento decorado

    def esBomba(self):
        return True

    def __str__(self):
        return "bomba"