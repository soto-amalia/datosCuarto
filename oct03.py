
#OBJETOS EN PYTHON 
#La clase mas simple qie se puede definir en Python es :


class nuevaClase():
    pass

""""""""""
En la consola:
$ python -i nueva_clase.py

>clase=nuevaClase
>print(clase)

Podemos añadir atributos a una clase sin hacerlo de forma explicita:




"""""""""



class Punto:
    pass

p1=Punto()
p2=Punto()

p1.x=10
p2.x=5
p1.y=1
p2.y=3
print(p1.x,p1.y),(p2.x,p2.y)

#La clase Punto es mas util si definimos comportamientos especificos:
#self es un punto cualquierade lo que esta en el inicio
class Punto: 
        def reset(self):
            self.x=0
            self.y=0
p=Punto()
p.reset()   

#def reset(self):
#self.mover(0,0)





 #Punto.reset(p)
print(p.x,p.y)

#Dentro de punto: 


def mover(self, x, y):
    self.x = x
    self.y = y

p = Punto()
p.mover(2, 2)
"""def mover(self,x,y):
     self.x=x
     self.y=y
p=Punto()
p.mover(2,2)
print(p.x,p.y)
"""

####Crear otor metodo que me calcule la distancia entre dos puntos, la distancia euclidiana
#Calcular la distancia lineal entre dos puntos 
## metodo dentro de la clase punto previamente definido 


##ESTRUCTURAS: EN c Las usamos para 
#listas en python puede contener diferentes tipos de datos 

##__var=0 variable privada

