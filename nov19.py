"""
RAW STRINGS 




---ejmplo Quiero encontrae un patron en espesifico dentro de la dena de texto y alomejor contar cuantos de 
esos patrones hay 
\r  ccorrimiento d ec
\b  backspace
\t caracter escape 
'\\' -- dara \ """

import re 
exp=re. compile("\ten")#--->
re.compile(r"\ten")

# Intentar con ("\\\\ten") o ("\\ten")
"""""cadenas duras: 'hola   r''hola, r'''hola''', r3comillashola3 comillas

"""""
print("hola === r'hola'") #false
print('\\the' == r'\the') #false
print('\the' == r'\the') #false



t="ten is not \ten, or \\ten \n".split('i')
"""EJEMPLO: Analizar archivos de texto que contengan una lista de nombres y
numeros telefonicos con el siguiente formato: 
apellido_paterno, nombre, apellido_materno: telefono
Puede que :
-NO exista el apellido materno
-EL telefono no contenga el codigo de area 
Asumir que los nombres y apellidos contienen letras y posiblemente guiones('-')
LOs telefonos tienen el formato: xx-xxxx-xxxx y los primeros 2 son opcionales"""


import re

# Patrón para analizar el formato: apellido_paterno, nombre, apellido_materno: telefono
patron = re.compile(
    r"([-a-zA-Z-]+",r"([-a-zA-Z-]+", r"([-a-zA-Z]+)?", r":(\d{2}-)-\d{4}-\d{4}")

#EL MAESTRO DICE QUE ESTO SI SE HACE [-a-z A-Z]+
#\d\d-\d\d\d\d-\d\d\d\d# Ejemplos de prueba de telefono

""" 

 telefono 
 \d{2}-\d{4}-\d{4}
 (\d{2}-)?\d{4}-\d{4}
 
 
Ahora
imprimiman lodsdatos 
y si usamos  r"?P<paterno>[-a-zA-Z]"
exp.gorup("paterno")

Y tambien vqa a convenir: 
y si usamos  r"(?P<paterno>[-a-zA-Z])"
r"(?P<materno>([-a-zA-Z]+)?"--- creo que este no 
el problema es que te va a a guardar en el espacio el materno  
r"((?P<materno>([-a-zA-Z]+))?"

"""
lineas = [
    "Garcia, Maria, Lopez: 12-3456-7890",
    "Martinez, Juan: 4567-8901",
    "Sanchez, Pedro, : 23-9876-5432",
    "Doe-Smith, John, Ann: 8765-4321",
    "Invalid, Example, Wrong: 123-456-789"  # Formato inválido
]

for linea in lineas:
    coincidencia = patron.match(linea)
    if coincidencia:
        apellido_paterno = coincidencia.group(1)
        nombre = coincidencia.group(2)
        apellido_materno = coincidencia.group(3) or ""  # Convertir None a cadena vacía
        telefono = coincidencia.group(4)
        
        print(f"Apellido Paterno: {apellido_paterno}")
        print(f"Nombre: {nombre}")
        print(f"Apellido Materno: {apellido_materno}")
        print(f"Teléfono: {telefono}")
        print("-" * 30)
    else:
        print(f"Formato inválido: {linea}")
        print("-" * 30)