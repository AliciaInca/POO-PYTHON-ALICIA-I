# Clase que gestiona personas y estudiantes

class GestorPersonas:
    def __init__(self):
        self.lista = []

    def agregar(self, persona):
        self.lista.append(persona)

    def mostrar_todos(self):
        for p in self.lista:
            print(p.mostrar_informacion())
