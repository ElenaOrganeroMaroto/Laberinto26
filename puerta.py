# puerta.py
from hoja import Hoja

class Puerta(Hoja):
    def __init__(self):
        super().__init__("Puerta") #Se le pasa el nombre que se le asigna a la hoja
        self.abierta = False
        self.lado1 = None
        self.lado2 = None
    
    def abrir(self):
        self.abierta = True
        
    
    def cerrar(self):
        self.abierta = False
        
    
    def entrar(self, alguien):
        if self.abierta:
            print("La puerta está abierta")
            # Determinar la otra habitación
            
        else:
            print("La puerta está cerrada")
            return None
    
   