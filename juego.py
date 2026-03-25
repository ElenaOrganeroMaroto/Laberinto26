from norte import Norte
from este import Este
from sur import Sur
from oeste import Oeste
from pared_bomba import ParedBomba
from bomba import Bomba
from pared import Pared
from puerta import Puerta
from personaje import Personaje
from habitacion import Habitacion

class Juego:
    def __init__(self):
        self.laberinto = None
        self.bichos = []      # OrderedCollection
        self.person = None
        self.hilos = {}       # Diccionario

    # --- acciones ---
    def abrirPuertas(self):
        def bloque(each):
            if each.esPuerta():
                each.abrir()
        self.laberinto.recorrer(bloque)

    def activarBombas(self):
        def bloque(each):
            if each.esBomba():
                each.activar()
        self.laberinto.recorrer(bloque)

    def cerrarPuertas(self):
        def bloque(each):
            if each.esPuerta():
                each.cerrar()
        self.laberinto.recorrer(bloque)

    def desactivarBombas(self):
        def bloque(each):
            if each.esBomba():
                each.desactivar()
        self.laberinto.recorrer(bloque)

    def agregarPersonaje(self, unaCadena):
        self.person = Personaje()
        self.person.nombre = unaCadena
        self.person.juego = self
        hab1 = self.obtenerHabitacion(1)
        hab1.entrar(self.person)


    # --- gestion-bichos ---
    def agregarBicho(self, unBicho):
        self.bichos.append(unBicho)

    def eliminarBicho(self, unBicho):
        self.bichos.remove(unBicho)

    def lanzarBicho(self, unBicho):
        print(unBicho, " se activa")

        # Definimos y guardamos el "proceso" 
        def proceso():
            while unBicho.estaVivo():
                unBicho.actua()        
        self.hilos[unBicho] = proceso

    def lanzarTodosLosBichos(self):
        print("Los bichos despiertan")
        for each in self.bichos:
            self.lanzarBicho(each)

    def terminarBicho(self, unBicho):
        unBicho.vidas = 0
        print(unBicho, "muere")

    def terminarTodosLosBichos(self):
        print("Los bichos terminan")
        for each in self.bichos:
            self.terminarBicho(each)
 
    
    # --- ataques ---
    def buscarPersonaje(self, unBicho):
        if unBicho.posicion == self.person.posicion:
            return self.person
        else:
            return None

    def muereBicho(self, unBicho):
        self.terminarBicho(unBicho)

    def muerePersonaje(self):
        print("Manmatao. Fin del juego")
        self.terminarTodosLosBichos()


    # --- factory method ---
    def asignarOrientaciones(self, unCont):
        unCont.orientaciones.append(self.fabricarNorte())
        unCont.orientaciones.append(self.fabricarEste())
        unCont.orientaciones.append(self.fabricarSur())
        unCont.orientaciones.append(self.fabricarOeste())


    def fabricarEste(self):
        return Este.default()

    def fabricarHabitacion(self, unNum=None):
        if unNum is None:
            return Habitacion()
        
        hab = Habitacion()
        hab.num = unNum
        self.asignarOrientaciones(hab)
        for each in hab.orientaciones:
            hab.ponerEn_elemento(each, self.fabricarPared())
        return hab

    def fabricarLab2Hab(self):
        from habitacion import Habitacion
        from puerta import Puerta
        from pared import Pared
        from laberinto import Laberinto
        hab1 = Habitacion()
        hab1.num = 1
        hab2 = Habitacion()
        hab2.num = 2
        puerta = Puerta()
        puerta.lado1 = hab1
        puerta.lado2 = hab2
        hab1.sur = puerta
        hab2.norte = puerta
        hab1.este = Pared()
        hab1.oeste = Pared()
        hab1.norte = Pared()
        hab2.este = Pared()
        hab2.oeste = Pared()
        hab2.sur = Pared()
        self.laberinto = Laberinto()
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

    def fabricarLab2HabBomba(self):
        from habitacion import Habitacion
        from puerta import Puerta
        from pared_bomba import ParedBomba
        from laberinto import Laberinto
        hab1 = Habitacion()
        hab1.num = 1
        hab2 = Habitacion()
        hab2.num = 2
        puerta = Puerta()
        puerta.lado1 = hab1
        puerta.lado2 = hab2
        hab1.sur = puerta
        hab2.norte = puerta
        hab1.este = ParedBomba()
        hab1.oeste = ParedBomba()
        hab1.norte = ParedBomba()
        hab2.este = ParedBomba()
        hab2.oeste = ParedBomba()
        hab2.sur = ParedBomba()
        self.laberinto = Laberinto()
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

    def fabricarLab2HabFM(self):
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        puerta = self.fabricarPuertaLado1_lado2(hab1, hab2)
        hab1.ponerEn_elemento(self.fabricarSur(), puerta)
        hab2.ponerEn_elemento(self.fabricarNorte(), puerta)
        self.laberinto = self.fabricarLaberinto()
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

    def fabricarLab4Hab2BmFM(self):
        from bomba import Bomba
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        hab3 = self.fabricarHabitacion(3)
        hab4 = self.fabricarHabitacion(4)
        p12 = self.fabricarPuertaLado1_lado2(hab1, hab2)
        p13 = self.fabricarPuertaLado1_lado2(hab1, hab3)
        p24 = self.fabricarPuertaLado1_lado2(hab2, hab4)
        p34 = self.fabricarPuertaLado1_lado2(hab3, hab4)
        hab1.sur = p12
        hab2.norte = p12
        hab1.este = p13
        hab3.oeste = p13
        hab2.este = p24
        hab4.oeste = p24
        hab3.sur = p34
        hab4.norte = p34
        bm1 = Bomba()
        hab1.agregarHijo(bm1)
        bm2 = Bomba()
        hab3.agregarHijo(bm2)
        self.laberinto = self.fabricarLaberinto()
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)

    def fabricarLab4HabFM(self):
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        hab3 = self.fabricarHabitacion(3)
        hab4 = self.fabricarHabitacion(4)
        p12 = self.fabricarPuertaLado1_lado2(hab1, hab2)
        p13 = self.fabricarPuertaLado1_lado2(hab1, hab3)
        p24 = self.fabricarPuertaLado1_lado2(hab2, hab4)
        p34 = self.fabricarPuertaLado1_lado2(hab3, hab4)
        hab1.sur = p12
        hab2.norte = p12
        hab1.este = p13
        hab3.oeste = p13
        hab2.este = p24
        hab4.oeste = p24
        hab3.sur = p34
        hab4.norte = p34
        self.laberinto = self.fabricarLaberinto()
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)

    def fabricarLaberinto(self):
        from laberinto import Laberinto
        return Laberinto()

    def fabricarNorte(self):
        return Norte.default()
    
    def fabricarSur(self):
        return Sur.default()

    def fabricarOeste(self):
        return Oeste.default()

    def fabricarPared(self):
        from pared import Pared
        return Pared()

    def fabricarPuerta(self):
        from puerta import Puerta
        return Puerta()

    def fabricarPuertaLado1_lado2(self, unaHab, otraHab):
        from puerta import Puerta
        puerta = Puerta()
        puerta.lado1 = unaHab
        puerta.lado2 = otraHab
        return puerta


    # --- accessing  ---
    def obtenerHabitacion(self, unNum):
        return self.laberinto.obtenerHabitacion(unNum)

