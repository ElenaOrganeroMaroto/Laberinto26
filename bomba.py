from decorator import Decorator

class Bomba(Decorator):
    def __init__(self, em=None, nombre="Bomba"):
        super().__init__(em, nombre)
        self.activa = False 

    def activar(self):
        print("Bomba activada")
        self.activa = True

    def desactivar(self):
        print("Bomba desactivada")
        self.activa = False

    #En python no podemos usar el mismo método con diferentes parámetros, entonces
    #si en alguien lo inicializamos con None provocamos que el parámetro sea opcional
    def entrar(self, alguien=None):
        if self.activa:
            if alguien is None: # Si no hay nadie, la bomba explota sin afectar a nadie
                print("Ha explotado una bomba")
            else:
                print(f"{alguien}, te ha explotado una bomba")
                # Habria que quitar vidas a alguien
        else:
            #No hace nada si está desactivada
            pass

    def esBomba(self) -> bool:
        return True