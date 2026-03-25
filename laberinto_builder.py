from norte import Norte
from sur import Sur
from este import Este
from oeste import Oeste

from noreste import Noreste
from noroeste import Noroeste
from sureste import Sureste
from suroeste import Suroeste

from juego import Juego
from laberinto import Laberinto

from bicho import Bicho
from agresivo import Agresivo
from perezoso import Perezoso

from armario import Armario
from puerta import Puerta
from habitacion import Habitacion
from pared import Pared
from bomba import Bomba

from cuadrado import Cuadrado


class LaberintoBuilder:
    def __init__(self):
        self.laberinto = None
        self.juego = None

    # --- accessing ---
    def asignarOrientaciones(self, unaForma):
        unaForma.orientaciones.append(self.fabricarNorte())
        unaForma.orientaciones.append(self.fabricarEste())
        unaForma.orientaciones.append(self.fabricarSur())
        unaForma.orientaciones.append(self.fabricarOeste())

    # --- factory method ---
    def fabricarAgresivo(self):
        return Agresivo()
    
    def fabricarArmario(self, unNum, unCont):
        arm = Armario()
        arm.num = unNum
        self.asignarOrientaciones(arm)
        
        for each in arm.orientaciones:
            arm.ponerEn_elemento(each, self.fabricarPared())
        
        pt = Puerta()
        pt.lado1 = arm
        pt.lado2 = unCont
        
        arm.ponerEn_elemento(self.fabricarEste(), pt)
        unCont.agregarHijo(arm)
        return arm

    def fabricarBichoModo_posicion(self, strModo, unNum):        
        nombre_metodo = f"fabricar{strModo}"
        metodo = getattr(self, nombre_metodo)
        modo = metodo() 
        
        hab = self.juego.obtenerHabitacion(unNum)
        bicho = Bicho()
        bicho.modo = modo
        
        hab.entrar(bicho)
        self.juego.agregarBicho(bicho)
        bicho.juego = self.juego

    def fabricarBombaEn(self, unCont):
        bm = Bomba()
        unCont.agregarHijo(bm)
        return bm

    def fabricarForma(self):
        forma = Cuadrado()
        self.asignarOrientaciones(forma)
        return forma

    def fabricarHabitacion(self, unNum):
        hab = Habitacion()
        hab.num = unNum
        hab.forma = self.fabricarForma()
        hab.forma.num = unNum
        
        for each in hab.forma.orientaciones:
            hab.ponerEn_elemento(each, self.fabricarPared())
        
        self.laberinto.agregarHabitacion(hab)
        return hab

    def fabricarJuego(self):
        self.juego = Juego()
        self.juego.laberinto = self.laberinto

    def fabricarLaberinto(self):
        self.laberinto = Laberinto()

    def fabricarPuertaLado1_or1_Lado2_or2(self, num1, unaOr, num2, otraOr):
        pt = Puerta()
        lado1 = self.laberinto.obtenerHabitacion(num1)
        lado2 = self.laberinto.obtenerHabitacion(num2)
        
        pt.lado1 = lado1
        pt.lado2 = lado2
        
        objOr1 = getattr(self, f"fabricar{unaOr}")()
        objOr2 = getattr(self, f"fabricar{otraOr}")()
        
        lado1.ponerEn_elemento(objOr1, pt)
        lado2.ponerEn_elemento(objOr2, pt)

    # --- Métodos de Orientación ---
    def fabricarNorte(self): return Norte.default()
    def fabricarSur(self):   return Sur.default()
    def fabricarEste(self):  return Este.default()
    def fabricarOeste(self): return Oeste.default()
    
    def fabricarNoreste(self):
        return Noreste.default()
    
    def fabricarNoroeste(self):
        return Noroeste.default()

    def fabricarSureste(self):
        return Sureste.default()

    def fabricarSuroeste(self):
        return Suroeste.default()

    def fabricarPared(self):
        return Pared()

    def fabricarPerezoso(self):
        return Perezoso()