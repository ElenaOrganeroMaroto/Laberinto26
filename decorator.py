#Decorator permite añadir funcionalidades a un objeto de forma dinámica, sin alterar su estructura. 
#Decorar un objeto de tipo Hoja, añadiendo una funcionalidad adicional.

from hoja import Hoja


class Decorator(Hoja):
    def __init__(self, em, nombre):
        super().__init__(nombre)  # Hereda de Hoja y pasa el nombre
        self.em = em

    def __str__(self):
        return "decorator"