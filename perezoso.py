import time
from modo import Modo

class Perezoso(Modo):
    def __init__(self):
        super().__init__()

    def duerme(self, unBicho):
        print(f"{unBicho} duerme")        
        time.sleep(3)

    def esPerezoso(self):
        return True

    def __str__(self):
        return "Perezoso"