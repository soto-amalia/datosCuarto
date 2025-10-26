"""""
Crear una clase que extienda a la clase 'dict'  de Python para que permita conocer
a la llave de mayor longitu de un diccionario



"""
 

class miDiccionario(dict):
    def clave_mas_larga(self):
        clave_larga=" "
        for clave in self.keys():
            if len(clave)>len(clave_larga):
                clave_larga=clave
        return clave_larga
    
#Crear un objeto de una prueba de nuestra clase
diccionarioPrueba=miDiccionario()#llamamos a la clase que extiende
diccionarioPrueba["uno"]=1#asignar tre elementos con llaves 
diccionarioPrueba["veiticuatro"]=24
diccionarioPrueba["tres"]=3
print("La llave mas larga es :", diccionarioPrueba.clave_mas_larga)

"""SOBREESCRIBIENDO ATRIBUTOS
"""
class Contacto:
    lista_contactos=ListaContactos()
    def __init__(self, nombre, email):
        self.nombre=nombre
        self.email=email
        Contacto.lista_contactos.append(self)
"""Podemos reemplazar o alterar el comportamiento de un método perteneciente a una superclase 
'sobreescribiendo' en una subclase"""
class Amigo(Contacto):
    def __init__(self, nombre, email, telefono):
        self.nombre=nombre
        self.email=email
        self.telefono=telefono


""
#Otra forma de sobreescribir atributos
class Amigo(Contacto):
    def __init__(self, nombre, email, telefono):
        super().__init__(nombre, email)
        self.telefono=telefono
"""POLIMORFISMO
El polimorfismo nos permite modificar el comportamiento de un método 
de una superclase dependioendo de sus subclases
"""
class Audio:
    def __init__(self, nombre):
        if not nombre.endswith(self.ext):
            raise Exception("Formato invalido")
        self.nombre=nombre

""
class MP3(Audio): 
    ext="mp3"
    def play(self):
        print(f"Reproduciendo {self.nombre} como mp3")
class WAV(Audio):
    ext="wav"
    def play(self):
        print(f"Reproduciendo {self.nombre} como un wav")
mp3=MP3("audio.mp3")
mp3.play()
""
mp3=MP3("audio.wav")

"""preguntamos si algo es subclase de la otra"""
am=Amigo("luis","luisQgmail.com","55")
isinstance(am,Contacto)#true
issubclass(Amigo,Contacto)#True 
isinstance(listaContactos(),)
#diagrama de clases de acuerdo de la aplicacion 
"""""""2""2"""""
"hacer analisis de datos ,
calentamiento global en ciertas regiones 

requerimiento, 
crear un moldelo 

objetos a analizar 
modelo o paquete exclusibvo a modelos u objetos para el analisis
extraccion, lectura  
refinar el diseño inicial 
hacer el pinche diagrama
tortas,
tortero
cliente 

"""""""""""""""""


class Flac:#Audio isisntance(flac(), Audio)
    def __init__(self, nombre):
        if not nombre.endswith("flac"):
            raise Exception("Formato incorrecto")
        self.nombre=nombre
    def play(self):
        print("Reproduciendo {0} como Flac".format(self.nombre))
