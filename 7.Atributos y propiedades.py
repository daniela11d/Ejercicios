
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  
        self.__edad = edad    

    @property
    def edad(self):
        return self.__edad  

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("La edad debe ser un número positivo.")

# Creamos un objeto de la clase Persona
persona = Persona("Juan", 30)

# Acceso directo a un atributo
print("Nombre:", persona.nombre)

# Acceso a una propiedad
print("Edad:", persona.edad)

# Modificamos la propiedad
persona.edad = 25
print("Nueva edad:", persona.edad)

# Intentamos establecer una edad negativa (lo cual no debería ser permitido)
persona.edad = -10
print("Nueva edad:", persona.edad)