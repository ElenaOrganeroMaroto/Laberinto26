from hoja import Hoja

class Pared(Hoja):
    def __init__(self):
        super().__init__("Pared")  #Se le pasa el nombre que se le asigna a la hoja

    def entrar(self,alguien):
        print("Has chocado con una pared")

    