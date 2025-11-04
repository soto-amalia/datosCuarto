"""""
Biblioteca Colibrí"""

from datetime import datetime, timedelta #libreria para usar el timepo actual
import uuid # para crear id unicos

# variables de Datos
libros = [] # Una Lista. Guarda todos los libros como diccionarios.
prestamos = [] # Lista que Guarda todos los préstamos (activos e históricos) como diccionarios.
_prox_id = 1 # contador para asignar IDs únicos a los libros.

def agregar_libro(titulo, autor, tipo, ejemplares=1):
    id_libro = str(uuid.uuid4())
    libros.append({
        "id": id_libro,
        "titulo":titulo, 
        "autor": autor, 
        "clasificacion":tipo,
        "copias":ejemplares
    })#append sirve para meter una sola cosa a una lista, pero puede ser otra lista o diccionario2
    return titulo

    #diccionario --- nombre:ALondra

print("Se creo correctamente la entrada del libro", agregar_libro("La comunidad del anillo", "Tolkien", "Fantasia"))
""""

def listar_libros() uan funcion que muestre lso libros que actualmente estan en al lista de libros
adentro de esa funcion un for
for libro in libros:
y un print de cada elemnto que quieras mostrar del libro actual;
despues
def prestar_libro(book_id, usuario, dias=14)
uan funcion que diga que libro due agarrado pro que usuario y cuantos dias
dentro de esa primerop valdiar si el libroe xiste
y si hya al menos una copia
"""""