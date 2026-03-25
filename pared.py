from hoja import Hoja

class Pared(Hoja):
    def __init__(self):
        super().__init__()

    def entrar(self, alguien=None):
        if alguien is None:
            print("Has chocado con una pared")
        else:
            print(f"{alguien} se ha chocado con una pared")