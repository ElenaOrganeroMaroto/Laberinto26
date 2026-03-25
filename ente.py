from abc import ABC, abstractmethod

class Ente(ABC):
    def __init__(self):
        self.vidas = 50
        self.poder = 1
        self.posicion = None
        self.juego = None

    def atacar(self):
        enemigo = self.buscarEnemigo()
        if enemigo is not None:
            enemigo.esAtacadoPor(self)

    @abstractmethod
    def buscarEnemigo(self):
        pass

    def esAtacadoPor(self, alguien):
        # Restamos las vidas según el poder del atacante
        self.vidas = self.vidas - alguien.poder
        
        print(f"{self} es atacado por {alguien}")
        print(f"vidas: {self.vidas}")
        
        if self.vidas <= 0: 
            self.muero()

    def estaVivo(self) -> bool:
        return self.vidas > 0

    @abstractmethod
    def muero(self):
        pass

    def __str__(self):
        return "Ente"