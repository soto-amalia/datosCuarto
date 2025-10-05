# Clase vacía de ejemplo
class nuevaClase:
    pass

# Ejemplo de usar la clase:
obj = nuevaClase()       # <- instancia (nota los paréntesis)
print(obj)               # muestra que es un objeto de nuevaClase


# Clase Punto con métodos útiles
class Punto:
    def __init__(self, x=0, y=0):
        # valores iniciales
        self.x = x
        self.y = y

    def reset(self):
        self.x = 0
        self.y = 0

    def mover(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # para imprimir bonito
        return f"Punto(x={self.x}, y={self.y})"


# Uso básico: atributos dinámicos (como en tu primer ejemplo)
p1 = Punto()
p2 = Punto()
p1.x = 10; p1.y = 1
p2.x = 5;  p2.y = 3
print((p1.x, p1.y), (p2.x, p2.y))  # imprime ambas tuplas correctamente

# Uso de los métodos definidos
p = Punto()
p.reset()          # deja (0, 0)
print(p.x, p.y)    # 0 0

p.mover(2, 2)      # ahora sí funciona porque mover está dentro de la clase
print(p.x, p.y)    # 2 2

print(p)           # usa __repr__: Punto(x=2, y=2)