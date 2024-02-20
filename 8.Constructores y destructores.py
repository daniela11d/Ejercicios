
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"Se ha creado una nueva instancia de Persona: {self.nombre}")

    def __del__(self):
        print(f"Se está destruyendo la instancia de Persona: {self.nombre}")

# Creación de objetos de la clase Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

# Liberación manual de memoria
del persona2