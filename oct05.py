import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def mover(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.x = 0
        self.y = 0

# Crear P1 en (0, 0)
print("Inicializando punto1 en (0, 0).")
punto1 = Punto(0, 0)
print(punto1.x,punto1.y)
# Mover P1 a (5, 6)
print("Moviendo punto1 a (5, 6).")
punto1.mover(5, 6)
print(punto1.x,punto1.y)
# Crear P2 
print("Inicializando punto2 en (3, 4).")
punto2 = Punto(3, 4)
print(punto2.x,punto2.y)

