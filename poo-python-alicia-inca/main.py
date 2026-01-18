from modelos.persona import Persona
from modelos.estudiante import Estudiante
from servicios.gestor import GestorPersonas

def main():
    gestor = GestorPersonas()

    persona1 = Persona("Carlos Pérez", 40)
    estudiante1 = Estudiante(
        "Alicia Inca",
        29,
        "Ingeniería en Tecnologías de la Información"
    )

    gestor.agregar(persona1)
    gestor.agregar(estudiante1)

    gestor.mostrar_todos()

if __name__ == "__main__":
    main()
