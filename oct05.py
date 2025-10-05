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
    #distancia= raiz {(x2​−x1​)cuadrado + (y2​−y1​)cuadrado} 
    def distancia(self, otro):
        dx = self.x - otro.x
        dy = self.y - otro.y
        return (dx**2 + dy**2) ** 0.5 # elevar al .5 o 1/2 es equivalente a raiz cuadrada

# Crear P1 en (0, 0)
print("Inicializando punto1 en:")
punto1 = Punto(0, 0)
print(punto1.x,punto1.y)

# Mover P1 a (5, 6)
print("Moviendo punto1 a:")
punto1.mover(5, 6)
print(punto1.x,punto1.y)

# Crear P2 
print("Inicializando punto2 en:")
punto2 = Punto(3, 4)
print(punto2.x,punto2.y)

# resetear P2 
print("Reiniciando punto2 en:")
punto2.reset()
print(punto2.x,punto2.y)

#distancia entre los puntos
print("La distancia es: ")
dist = punto1.distancia(punto2)
print(dist) 

distancia2 = punto2.distancia(punto1)
print(distancia2)