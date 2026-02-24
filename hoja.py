#Hoja

from elemento_mapa import ElementoMapa


class Hoja(ElementoMapa):
    def __init__(self, nombre: str):
        super().__init__() #Hereda de ElementoMapa
        self.nombre: str = nombre #Nombre es un atributo que guarda el nombre de la hoja: puerta, pared, ...

    def __str__(self):
        return self.nombre

   