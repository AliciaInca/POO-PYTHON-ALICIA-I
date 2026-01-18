# Clase derivada Estudiante
# Aplica herencia y polimorfismo

from modelos.persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    # Polimorfismo: sobrescritura del método
    def mostrar_informacion(self):
        return (
            f"Nombre: {self.get_nombre()}, "
            f"Edad: {self.get_edad()}, "
            f"Carrera: {self.carrera}"
        )
