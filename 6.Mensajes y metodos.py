
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.bandeja_entrada = []

    def enviar_mensaje(self, destinatario, mensaje):
        destinatario.recibir_mensaje(self, mensaje)

    def recibir_mensaje(self, remitente, mensaje):
        self.bandeja_entrada.append((remitente, mensaje))

    def ver_bandeja_entrada(self):
        print(f"Bandeja de entrada de {self.nombre}:")
        for remitente, mensaje in self.bandeja_entrada:
            print(f"De: {remitente.nombre}\nMensaje: {mensaje}")

# Creamos dos usuarios
usuario1 = Usuario("Juan")
usuario2 = Usuario("María")

# Juan envía un mensaje a María
usuario1.enviar_mensaje(usuario2, "Hola, María. ¿Cómo estás?")

# María ve su bandeja de entrada
usuario2.ver_bandeja_entrada()