#MODULOS Y PAQUETES: Un modulo en python es todo aquel archivo con la extension ".py"


"""productos.py
base_datos.py
    Database(clase)
    ----dentro de productos.py
import base_datos.Database    ---bd=bada_datos.Database()
se puede usar. conection   --- bd=BD()
from base.dato import Database as BD 
IMPORT BASE_DATOS
bd=base_datos.Database()
from base_datos import *--- casi no se usa ---bd=Database()


En productos.py
from base_datos import *
En base_datos.py
from productos import *
bd=Database()




"""
import this 

#
"""Un paquete es una coleccion de modulos intercnectados y alojados en una carpeta.
Python identifica a una carpeta como paquete, si esta contiene un archivo llamado "__int__.py".

"""

"""Rutas absolutas 
#import math.misellaneous
from math import miscellaneous
f= math.miscellaneous.Factorial()
f=miscellaneous.Factorial()
from math.miscellanrous import Factorial as F
f=Factorial
"""
"""""""""""""""

#Usaremos funcion que se llama factorial
directorio_raiz/
    main.py
    math/
        __int__.py
        database.py   
        miscellaneous.py
        matrix/
        __int__.py
        basics.py
        determinants.py
        inverse.py
        statistics/
        __int__.py
        basics.py
        models.py
        time_series.py



""
/
home/
    luis/
        Documentos/
            tarea.txt
            escuela/
                desarrollo/
                tarea1.txt
    documentos(archivo)


/(raiz)home/luis/Documentos/tarea.txt --->subdirectorios donde se pueden editar archivos de texto
documentos y de ahi escuela/
/luis
nano./Documentos/tarea.txt
.--->directorio actual
nano../tarea.txt --->vete un paso atras y abreme el archivo que esta 
"""





#from .miscellaneous import Factorial (math)
# Ubicacion actual miscellaneous 
#from ..miscellaneous import Factorial  (matrix)

# dos puntos regresa la direccion
# Estas dos scrips son relativas 
"""""
from math.matrix import inverse
name main():
if __name__ =='__main__':
    main()
"""""
# BUsca el identificador con el nombre de name y la importacion se va a ir directo a main


""""" 
MIERCOLES 08 DE OCUTUBRE 2025
CONTROL DE ACCESO 
Todos los atributos y metodos destro de una clase en Python son, en esencia, publicos.
Sin embargo hay formas de indicar que estos tributos y metodos sean "privados" usando los simbolos '_'(privado)
o '__'(muy privado), pero no significa que estos sean inaccesibles para cualquier usuario.
Por ejemplo: 

"""

class Secreto:
    def __init__(self, secreto, password):
        # atributos "privados" (nombre con double underscore -> name mangling)
        self.__secreto = secreto  #secreto es un name mangling
        self.__password = password

    def decifrar(self, cadena):
        # comparar la cadena con la contraseña y devolver el secreto si coincide
        if cadena == self.__password:
            return self.__secreto
        return ""

secreto = Secreto("Top secret", "Qwerty")  # "Qwerty" es la contraseña
print(secreto.decifrar("Qwerty"))  # debe imprimir "Top secret"

# Intento de acceder al atributo privado desde fuera:
# print(secreto.__secreto)  # esto provocaría AttributeError
# Forma "no recomendada" pero válida: acceder usando name mangling
print(secreto.__Secreto)  # Imprimira EXCEPTION
print(secreto._Secreto__secreto)  # muestra también "Top secret" 


"""""
HERENCIA BASICA
Todas las clases en Python son subclases de la clase llamada "Onject",
"""
class MiClase(object):
    pass

# que es equivalente a
class MiClase:
    pass
# Por ejemplo: Creemos que una clase que sirva como agenda, llamada "Contacto"
class Contacto:
    lista_contactos=[] #variable de clase

    def __init__(self, nombre, email):
        self.nombre=nombre
        self.email=email
        Contacto.lista_contactos.append(self)

#
"""" scope
a=5               def a:
                    a=5+1
b=fun(a)
    pritn(b)##6 VIene de la funcion a no de a la variable 


"""""
class Distribuidor(Contacto):
    def ordenar(self, orden,n):
        print(f"Se han pedido {n} de {orden} para{self.nomre}")

c1=Contacto("luis","luis@gmail.com")

c2=Distribuidor("ana","ana@gmail.com")
print(c1.lista_contactos) #[Contacto, Distribuidor]
print(c2.lista_contactos)  #[Contacto, Distribuidor]
print(c1.ordenar("pastor",5)) #Exception 
print(c2.ordenar("suadero",5))#Se han pedido 5 de suadero para ana 



# EXTENDIENDO TIPOS PREDEFINIDOS 
#extender , con objetos de tipo lista para
class ListaContactos(list):
    def buscar(self, nombre):
        encontrados=[]
        for c in self:#self es un obkjeto de lista, tipo lista
            if nombre in c.nombre: 
                encontrados.append(c)
        return encontrados

# MOdificar clase contacto par ausar listaContactos 
class Contacto2:
    lista_contactos=ListaContactos()

    def __init__(self, nombre, email):
        self.nombre=nombre
        self.email=email
        Contacto.lista_contactos.append(self)


# list(clase), [](clase) se supone son lo mismo
#Vamos a crear 3 contactos distintos 
c1=Contacto("alejandra","ale@gmail.com")
c2=Distribuidor("ana","ana@gmail.com")
c3=Contacto("joseline","jos@gmail.com")


# queremos que regrese alejandra 
c=[e.nombre for e in Contacto.Lista_contactos.buscar("alejandra")]
# 
# #
