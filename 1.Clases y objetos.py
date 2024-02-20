
# Definición de la clase 'Persona'
class Persona:
    # Método inicializador
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método para imprimir los detalles de la persona
    def imprimir_detalles(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# Creación de objetos (instancias) de la clase Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

# Imprimir detalles de las personas
print("Detalles de la Persona 1:")
persona1.imprimir_detalles()

print("\nDetalles de la Persona 2:")
persona2.imprimir_detalles()