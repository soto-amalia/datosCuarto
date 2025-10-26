
#Modelo Orientado a Objetos de lugares reales, de puntos de interes  diario.



class Lugar: 
    def __init__(self,ubicacion, nombre):
        self.nombre=nombre
        self.ubicacion=ubicacion
    def mostrar(self):
        print("EL lugar es: ", self.nombre," y esta en:", self.ubicacion)
#Crear una clase heredada pòr subclase de la principal

class Comida(Lugar):
    def __init__(self,ubicacion, nombre, tipo):
        super().__init__(ubicacion, nombre)
        self.tipo=tipo
    def tomarPedido(self):
        print("Tu pedido ha sido ordenado de el restaurante ", self.nombre)
    def mostrar(self):
        print("EL lugar se llama : ", self.nombre," y esta en:", self.ubicacion," vende: ",self.tipo)

class Restaurante(Comida):
    def __init__(self,ubicacion, nombre, tipo, especialidad):
        super().__init__(ubicacion, nombre, tipo)
        self.especialidad=especialidad
    def Especialidad(self):
        print("La especialidad del restaurante es", self.especialidad)

l=Lugar("rumbera","melchor")
l.mostrar()
l2=Comida("el camote","puebla","sushi")
l2.mostrar()
l2.tomarPedido()
l3=Restaurante("los pollos bonitos","tlatelolco","pollo frito","pollo habanero")
l3.mostrar()
l3.Especialidad()

