"""
HERENCIA 
LA HERENCIA ES UNA RELACION QUE NOS PERMITE CREAR UNA CLASE A PARTIR DE OTRA.
Esta nueva clase se conoce como "subclase" o "clase hija". La subclase contendrá
los atributos y mètodos de la "subclase" por lo que las subclases expamden o extiende el 
comportamiento de la superclase.

Tablero
Clase: Piezas    Set: Set de Ajedrez---- mover(tablero)---Clase abstracta
Subclase:
Peon: Forma , metodo---mover()
Alfil: Forma, mover()
Caballo: Forma, mover()
Reina: Forma, mover()---- polimorfismo
Rey: Forma, mover()--- polimorfismo
Torre: Forma, mover()--- subescriben a mover()
Polimorfismo----- principio de la programación que permite que objetos de diferentes tipos respondan al mismo mensaje de manera única y específica
Python--Duck TYping- Tipado dinamico 

HERENCIA(CASO DE USO)
Requerimiento:La libreria local ha solicitado actualizar o crear un nuevo catalogo porque 
el actual es ineficiente y esta desordenada.
1.Análisis:
Revisar o buscar a quien sabe sonbre la libreía local
Usualmente se hace la busquedfa de libros por autor, título, ID, editorial, edicion 
-Los libros de identifican por su ISBN
-Dentro de la libreria se usa el sistema decimal Dewey (DDS)
2. Diseño:
Libros: ISBN, DDS, Titulo, autor, género 
Autor: Nombre, 
Catalogo: DIsponibilidad 
3. Programacion:


CATALOGO
Disponibilidad: int
metodo- buscar(libro)

LIBROS
ISBN
Titulo
autor(es)
genero 
DDS

AUTOR
Nombre

Puede haber revistas, comics, 
En la siguiente interaccion el cliente comenta que en la libreria tambien se tienen DVD's, Revistas y CD's.
Estos elementos no tienen ISBN o DDS asociado.
EN su lugar  se una un Codigo universal de Producto (UPC)
Además 
-Los CD's se organizan por autor 
-Los DVD's se organizan por titulo y genero 
-Las revistas por título, volumen y almacen de publicacion 
-Los libros por DD's

Catálogo: --- se conecta a producto
buscar(Producto)
Producto:--- se conecta a libro, revista, cd y dvd y a Contrubuidor
    UPC 
    titulo
    tema
    contrinuidor
Localizar--- metodo 
Obtenr COntribuidor 

Contribuidor:--- se conecta a libro, revista, cd y dvd o ---- solo a tipo 
contribuir y asise elimina auror y productor, director de los porductos
nombre
Tipo contribuidor:  Ahi ya tendriamos a autor, director, escritor, etc  


Tipo Contribuidor 
contribuidor:Contribuidor 
tipo 

Libro:
    ISBN
    genero 
    DD's
    Autor
DVD:
    genero
    año
    DIrectores
    Autor
    Escritor
Revista:
    vulumen
    año
    nom de publicacion
    Editor
    Escritor
CD
    genero
    año
    Artista
    Productora 
Utilizar polimorfismo 
-----SEÑOR --- El usuario ingresa
Retorna opciones 
El señor d elos anillos
EL señor de las moscas 
EL señor de los cielos 
señorita 
 agragar cordinalidad, argumentos, tipos, metodos con argumentos, si no hay retorno
 hacer un diagrama
"""


