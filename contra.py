


class Usuario:
    def __init__(self, nombre, contrasena):
        self._nombre = nombre
        self.contrasena = contrasena

    def inicioSesion(self, intento):
        if intento== self.contrasena:
            return ("Hola bienvenido ")
        else:
            return ("Contraseña incorrecta ")
amal17=Usuario("Amalia","Sushi123")
print(amal17.inicioSesion("Sushi1"))
print(amal17.inicioSesion("Sushi123"))