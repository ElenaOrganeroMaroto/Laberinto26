#Elemento Mapa está implementado con Composite, es decir, cada elemento del mapa puede contener otros elementos del mapa. 
#Esto permite crear estructuras jerárquicas de elementos del mapa, como habitaciones que contienen puertas.

from abc import ABC, abstractmethod

class ElementoMapa(ABC):
    def __init__(self):
        self.padre = None

    @abstractmethod
    def entrar(self, alguien):
        pass  #Pass, es el no hacer nada 

    def esBomba(self):
        return False
    
    def esPuerta(self):
        return False

    @abstractmethod
    def recorrer(self, func):
        func(self) #Delega la responsabilidad a sus hijos 

    def __str__(self):
        return "ElementoMapa" 
    