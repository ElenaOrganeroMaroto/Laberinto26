import json 
from laberinto_builder import LaberintoBuilder
from laberinto_builder_rombo import LaberintoBuilderRombo

class Director:
    def __init__(self):
        self.builder = None
        self.dict = None

    def leerArchivo(self, unArchivo):
        with open(unArchivo, 'r', encoding='utf-8') as f:
            self.dict = json.load(f)

    def iniBuilder(self):
        #Aquí decidimos qué tipo de Builder usar según la forma
        forma = self.dict.get('forma')
        
        if forma == 'poligono4':
            self.builder = LaberintoBuilder()
        elif forma == 'rombo':
            self.builder = LaberintoBuilderRombo()

    def fabricarLaberinto(self):
        self.builder.fabricarLaberinto()
        
        for cada_elemento in self.dict.get('laberinto', []):
            self.fabricarLaberintoRecursivo(cada_elemento, 'root')
        
        # Fabricar las puertas
        for cada_puerta in self.dict.get('puertas', []):
            self.builder.fabricarPuertaLado1_or1_Lado2_or2(
                cada_puerta[0], cada_puerta[1], cada_puerta[2], cada_puerta[3]
            )

    def fabricarLaberintoRecursivo(self, unDic, padre):
        con = None
        tipo = unDic.get('tipo')

        # Contenedores
        if tipo == 'habitacion':
            con = self.builder.fabricarHabitacion(unDic.get('num'))
        elif tipo == 'armario':
            con = self.builder.fabricarArmario(unDic.get('num'), padre)
        
        # Hojas 
        elif tipo == 'bomba':
            con = self.builder.fabricarBombaEn(padre)

        # Hijos recursivos: 
        hijos = unDic.get('hijos', [])
        for cada_hijo in hijos:
            self.fabricarLaberintoRecursivo(cada_hijo, con)

    def fabricarJuego(self):
        self.builder.fabricarJuego()

    def fabricarBichos(self):
        bichos = self.dict.get('bichos', [])
        for cada_bicho in bichos:
            self.builder.fabricarBichoModo_posicion(
                cada_bicho.get('modo'), 
                cada_bicho.get('posicion')
            )

    def obtenerJuego(self):
        return self.builder.juego

    def procesar(self, unArchivo):
        self.leerArchivo(unArchivo)
        self.iniBuilder()
        self.fabricarLaberinto()
        self.fabricarJuego()
        self.fabricarBichos()