from laberinto import Laberinto
from habitacion import Habitacion
from pared import Pared
from puerta import Puerta
from pared_bomba import ParedBomba
from bomba import Bomba

class Juego:
    def __init__(self):
        self.bichos = []  # OrderedCollection new
        self.laberinto = None
    

    
    #--------- BOMBAS ---------
    def activar_bombas(self):
        if self.laberinto:
            for elemento in self.laberinto.hijos:
                # Preguntamos: ¿este elemento es una bomba?
                if hasattr(elemento, 'esBomba') and elemento.esBomba():
                    elemento.activar()


    def desactivar_bombas(self):
        if self.laberinto:
            for elemento in self.laberinto.hijos:
                # Preguntamos: ¿este elemento es una bomba?
                if hasattr(elemento, 'esBomba') and elemento.esBomba():
                    elemento.desactivar()
    

    #--------- BICHOS ---------
    def agregar_bicho(self, un_bicho):
        self.bichos.append(un_bicho)
    
    def eliminar_bicho(self, un_bicho):
        if un_bicho in self.bichos:
            self.bichos.remove(un_bicho)
            return un_bicho
        return None
    
    def get_bichos(self):
        """Devuelve la lista de bichos"""
        return self.bichos
    

    
    #--------- FABRICACIÓN ---------
    def fabricar_habitacion(self):
        """Crea una nueva habitación sin número"""
        return Habitacion(0)  # Número por defecto
    
    def fabricar_laberinto(self):
        """Crea un nuevo laberinto"""
        return Laberinto()
    
    def fabricar_pared(self):
        """Crea una nueva pared"""
        return Pared()
    
    def fabricar_puerta(self):
        """Crea una nueva puerta"""
        return Puerta()


    # --------- LABERINTO ---------
    def get_laberinto(self):
        return self.laberinto
    
    def set_laberinto(self, laberinto):
        self.laberinto = laberinto


    #--------- HABITACIÓN ---------
    def obtener_habitacion(self, un_num):
        """Obtiene una habitación por su número"""
        if self.laberinto:
            return self.laberinto.obtener_habitacion(un_num)
        return None
    

    #-------- EJEMPLOS ---------
    def fabricar_habitacion_con_num(self, un_num):
        """Crea una nueva habitación con número y paredes"""
        hab = Habitacion(un_num)
        hab.norte = self.fabricar_pared()
        hab.este = self.fabricar_pared()
        hab.oeste = self.fabricar_pared()
        hab.sur = self.fabricar_pared()
        return hab
    
    
    
    def fabricar_puerta_con_lados(self, una_hab, otra_hab):
        """Crea una puerta conectando dos habitaciones"""
        puerta = self.fabricar_puerta()
        puerta.lado1 = una_hab
        puerta.lado2 = otra_hab
        return puerta
    

    def fabricar_lab2hab(self):
        """Crea un laberinto de 2 habitaciones con paredes bomba"""
        hab1 = Habitacion(1)
        hab2 = Habitacion(2)
        
        puerta = self.fabricar_puerta()
        puerta.lado1 = hab1
        puerta.lado2 = hab2
        
        hab1.sur = puerta
        hab2.norte = puerta
        
        # Paredes bomba en habitación 1
        hab1.este = ParedBomba()
        hab1.oeste = ParedBomba()
        hab1.norte = ParedBomba()
        
        # Paredes bomba en habitación 2
        hab2.este = ParedBomba()
        hab2.oeste = ParedBomba()
        hab2.sur = ParedBomba()
        
        self.laberinto = self.fabricar_laberinto()
        self.laberinto.agregar_habitacion(hab1)
        self.laberinto.agregar_habitacion(hab2)
    


    def fabricar_lab2hab_fm(self):
        """Crea un laberinto de 2 habitaciones usando métodos de fábrica"""
        hab1 = self.fabricar_habitacion_con_num(1)
        hab2 = self.fabricar_habitacion_con_num(2)
        
        puerta = self.fabricar_puerta_con_lados(hab1, hab2)
        
        hab1.sur = puerta
        hab2.norte = puerta
        
        self.laberinto = self.fabricar_laberinto()
        self.laberinto.agregar_habitacion(hab1)
        self.laberinto.agregar_habitacion(hab2)
    


    def fabricar_lab4hab_fm(self):
        """Crea un laberinto de 4 habitaciones"""
        hab1 = self.fabricar_habitacion_con_num(1)
        hab2 = self.fabricar_habitacion_con_num(2)
        hab3 = self.fabricar_habitacion_con_num(3)
        hab4 = self.fabricar_habitacion_con_num(4)
        
        p12 = self.fabricar_puerta_con_lados(hab1, hab2)
        p13 = self.fabricar_puerta_con_lados(hab1, hab3)
        p24 = self.fabricar_puerta_con_lados(hab2, hab4)
        p34 = self.fabricar_puerta_con_lados(hab3, hab4)
        
        hab1.sur = p12
        hab2.norte = p12
        
        hab1.este = p13
        hab3.oeste = p13
        
        hab2.este = p24
        hab4.oeste = p24
        
        hab3.sur = p34
        hab4.norte = p34
        
        self.laberinto = self.fabricar_laberinto()
        self.laberinto.agregar_habitacion(hab1)
        self.laberinto.agregar_habitacion(hab2)
        self.laberinto.agregar_habitacion(hab3)
        self.laberinto.agregar_habitacion(hab4)
    


    def fabricar_lab4hab2bm_fm(self):
        """Crea un laberinto de 4 habitaciones con 2 bombas"""
        hab1 = self.fabricar_habitacion_con_num(1)
        hab2 = self.fabricar_habitacion_con_num(2)
        hab3 = self.fabricar_habitacion_con_num(3)
        hab4 = self.fabricar_habitacion_con_num(4)
        
        p12 = self.fabricar_puerta_con_lados(hab1, hab2)
        p13 = self.fabricar_puerta_con_lados(hab1, hab3)
        p24 = self.fabricar_puerta_con_lados(hab2, hab4)
        p34 = self.fabricar_puerta_con_lados(hab3, hab4)
        
        hab1.sur = p12
        hab2.norte = p12
        
        hab1.este = p13
        hab3.oeste = p13
        
        hab2.este = p24
        hab4.oeste = p24
        
        hab3.sur = p34
        hab4.norte = p34
        
        bm1 = Bomba(hab1)  
        hab1.agregar_hijo(bm1)
        
        bm2 = Bomba(hab3)
        hab3.agregar_hijo(bm2)
        
        self.laberinto = self.fabricar_laberinto()
        self.laberinto.agregar_habitacion(hab1)
        self.laberinto.agregar_habitacion(hab2)
        self.laberinto.agregar_habitacion(hab3)
        self.laberinto.agregar_habitacion(hab4)
    


    
    
    