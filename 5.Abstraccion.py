
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se depositaron {cantidad} unidades. Saldo actual: {self.saldo}")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se retiraron {cantidad} unidades. Saldo actual: {self.saldo}")
        else:
            print("Fondos insuficientes.")

# Creamos una cuenta bancaria
mi_cuenta = CuentaBancaria("Juan Pérez", 1000)

# Realizamos algunas operaciones
mi_cuenta.depositar(500)
mi_cuenta.retirar(200)
mi_cuenta.retirar(1500)  # Intentamos retirar más de lo que tenemos