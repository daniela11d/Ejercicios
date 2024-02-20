
# Definición de la clase base 'Vehiculo'
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

# Definición de la clase derivada 'Automovil', que hereda de 'Vehiculo'
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, color):
        # Llamada al constructor de la clase base
        super().__init__(marca, modelo)
        self.color = color

    def mostrar_info(self):
        # Llamada al método de la clase base
        super().mostrar_info()
        print(f"Color: {self.color}")

# Creación de un objeto de la clase derivada 'Automovil'
auto = Automovil("Toyota", "Corolla", "Rojo")

# Acceso a métodos de la clase base y derivada
auto.mostrar_info()