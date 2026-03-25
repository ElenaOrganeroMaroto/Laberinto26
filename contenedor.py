from elemento_mapa import ElementoMapa

class Contenedor(ElementoMapa):
    def __init__(self):
        super().__init__() 
        self.num = None
        self.hijos = [] #OrderedCollection new
        self.forma = None
        self.orientaciones = []
    

    # --- Gestión de Hijos ---
    def agregarHijo(self, unEM):
        self.hijos.append(unEM)

    def eliminarHijo(self, unEM):
        self.hijos.remove(unEM)
     

    # --- Gestión de Orientaciones ---
    def agregarOrientacion(self, unaOr):
        self.forma.agregarOrientacion(unaOr)

    def eliminarOrientacion(self, unaOr):
        self.forma.eliminarOrientacion(unaOr)

    def obtenerOrientacionAleatoria(self):
        return self.forma.obtenerOrientacionAleatoria()

    def ponerEn_elemento(self, unaOr, unEM):
        self.forma.ponerEn_elemento(unaOr, unEM)


    # --- Acciones ---
    def entrar(self, alguien):
        print(f"{alguien} está en {self}")
        alguien.posicion = self

    def irAlNorte(self, alguien):
        self.forma.irAlNorte(alguien)


    # --- Iterator ---
    def recorrer(self, unBloque):
        unBloque(self) 
        
        # Primero recorremos los hijos
        for cada_hijo in self.hijos:
            cada_hijo.recorrer(unBloque)
            
        # Luego recorremos las orientaciones
        if self.forma:
            for cada_or in self.forma.orientaciones:
                cada_or.recorrer_enContenedor(unBloque, self.forma)
        
