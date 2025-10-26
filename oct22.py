"""""
Miércoles 22 de Octubre 2025
EJEMPLO HDF5
"""
import numpy as np
import h5py 
#pip installl h5py 

datos=np.random.random(1000)
with h5py.FIle("test.hdf5","w")as f:
    dset=f.crate_dataset("default", data=datos)

with h5py.File("test.hdf5","r")as f:
    dat=f["default"]
    print(min(dat))
    print(max(dat))
    print(dat[:15])
""""JASON(JAVASCRIPT OBJECT NOTATION )
Es un formato en texto plano ligero usando para compartir información de forma eficiente.
La ventaja principal de este formato es que es independiente de la plataforma donde sea creado.
Un JSON contiene dos estructuras:
    -Una coleccion de paras llave-valor 
        -diccionario
        -struct
        -registro 
    -Una lista odenada de valores 
        -lista
        -arreglo
        -vector 
Un objeto es un conjunto de pares llave-valor:
    -Un objeto se delimita con "{}"
    -La llave y el valor estàn separados por ' ', e.g. 'nombe:'ana'
    -Cada par esta separado por una como ','.
Un arreglo es una colección odenada de valores: 
    -UN arreglo se delimita con '[]'
    -Cada elemento del arreglo está separado por una coma ','.
UN valot puede ser un string, un numero, un booleano, un arreglo
o un objeto y se pueden anidar indefindamente.

OBJETO 
    -Cliente
    -Direccion
PROPIEDAD 
    -Nombre 
    -Apellido(s)
    -Calle
    -Municipio
    -Estado
    -C.P.
    -Telèfono[0]
    -Telèfono[1]
VALORES
    -Ana
    -Méndez Martinez 
    -Etén
    -Guatavo A. Madero 
    -CDMX
    -07720
    -5512345678
    -5687654321
Tomar ejemplos y transformarlo a json 



"""
{
    "Nomnbre":"Ana",
    "Apellido": "Mendez Martinez",
    "Direccion":{
        "Calle":"Etén",
        "Municipio":"Gustavio A. Madero",
        "Estado":"CDMX",
        "C.P.":"07220",
    },
    "Telefono":{
        "55 1234 5787"
        "56 8765 4321"

    }
}
#SEGUNDO EJEMPLO 
import json
obj='''{"nombre":"ana", 
        "tel":{"tipo":"intil", "numero":"+52 5562},
        "email":["ana@gmail.com","ana@ipn.mx"]
        }'''
dat=json.loads(obj)
nombre=dat["nombre"]
tel=dat["tel"]["tipo"]
jdumpo=json.dumps(dat, indent=4)#serializacions
with open("datos.json","w") as f:
    f.write(jdumpo)


#series de tiempo 

