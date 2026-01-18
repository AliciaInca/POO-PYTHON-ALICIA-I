# Clase base Persona
# Se aplica encapsulación con atributos privados

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # atributo privado
        self.__edad = edad      # atributo privado

    # Métodos getter (encapsulación)
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    # Método que será sobrescrito (polimorfismo)
    def mostrar_informacion(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"
