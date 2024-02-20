
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  
        self.__edad = edad      

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("La edad debe ser un número positivo.")

# Creación de un objeto de la clase Persona
persona = Persona("Juan", 30)

# Acceso controlado a los atributos mediante métodos
print("Nombre:", persona.get_nombre())  
print("Edad:", persona.get_edad())      

# Modificación de los atributos mediante métodos
persona.set_nombre("Carlos")  # Modificando el nombre mediante un método
persona.set_edad(-25)         # Intentando modificar la edad con un valor negativo
print("Nuevo nombre:", persona.get_nombre())  
print("Nueva edad:", persona.get_edad())      