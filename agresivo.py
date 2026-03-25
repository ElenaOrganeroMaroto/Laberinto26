import time
from modo import Modo 

class Agresivo(Modo):
    
    def duerme(self, unBicho):
        print(f"{unBicho} duerme")
        time.sleep(1) # Es el Delay de Pharo

    def esAgresivo(self) -> bool:
        return True

    def __str__(self):
        return "Agresivo"