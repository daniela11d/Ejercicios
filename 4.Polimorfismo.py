
# Definición de la clase base 'Animal'
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

# Definición de la clase derivada 'Perro'
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

# Definición de la clase derivada 'Gato'
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Función que usa polimorfismo
def hacer_sonido_animal(animal):
    return animal.hacer_sonido()

# Creación de objetos de diferentes clases
perro = Perro("Buddy")
gato = Gato("Whiskers")

# Uso de la función con diferentes objetos
print(perro.nombre + ": " + hacer_sonido_animal(perro))
print(gato.nombre + ": " + hacer_sonido_animal(gato))