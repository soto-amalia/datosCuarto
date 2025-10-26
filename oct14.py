"""""
CLASES ABSTRACTAS 
"""
class Flac:#Audio isisntance(flac(), Audio)
    def __init__(self, nombre):
        if not nombre.endswith("flac"):
            raise Exception("Formato incorrecto")
        self.nombre=nombre
    def play(self):
        print("Reproduciendo {0} como Flac".format(self.nombre))
"""""
Las clases abstractas "base" o ABCs son clases que permiten especificar las condiciones  necesarias 
para usar el duck typing.
En estas clases se definen los métodos y porpiedades que de cumplir una clase para ser considerada como
subclase de una superclase
La clase 'Container' es la clase abstracta más simple en Python.
#En la terminal 
> from calllections import Container
>Container__abstractimethods__
frocenset(["__contains__"])
Podemos definir una clase(contenedor) que verifiquen si un valor pertenece al conjunto de números 
enteros impares:"""

class Impares:
    def __contains__(self, n):
        if not isinstance(n,int) or not n%2:#n seas 0 o no sea par
            return False
        return True
from collections import Container 

numero_impar=Impares()
isinstance(numero_impar,Container)#True
issubclass(Impares,Container)#True


1 in numero_impar#__contains__ True
2 in numero_impar#false
3 in numero_impar#true
"hola" in numero_impar#false 


import abc
class Multimedia(metaclass=abc.ABCmeta):
    @abstractmethod #Decorador abstracto
    def play():#defirnir metodo abstracto
        pass #definir propiedades 
    
    @abstractproperty
    def ext():
        pass
        
    @classmethod
    def __subclasshook__(cls, C):#cls subclase
        if cls in Multimedia: #la clase es multimedia ? 
            att=set(dir(C))#contruye un set y trata de comparar con subclase
            if set(cls, __abstractmethods__)<=att:
                return True
    raise NotImplemented

#en la terminal 
class Wav(Multimedia):
    pass
w=Wav()#Exception falta:ext play
class Ogg: 
    ext='ogg'
    def play(self):
        pass
o=Ogg()
#NO es necesario aplicar una clase abstracta en la aplicacion 

#las clases abtractas defunen condiciones epecificas 