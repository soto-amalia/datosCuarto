"""
PANDAS(PANEL DATA)
lIBRERÍA PARA LA MANIPULACION Y ANALISIS DE DATOS
pip install pandas
Este paquete contiene: 
-Metodos para la carga de datos 
-Manejo y creacion de DataFrames indexados 
-Manejo de datos 'nulos' o faltantes 
-Mezcla, agrupacion, filtrado y transformacion de datos
-Manejo de seies de tiempo 

SERIES 
Estructura unidimensional que puede contener cualquier tipo de dato 
En escala se les llama rrdds
Version distribuida del orden de los datos 
Sistemas distribuidos, dts, concatenar infromacion y como procesarla adecuadamente 
Series unidimencionales
Parecido a como funcionan tablar relacionales

"""

import pandas as pd
import numpy as np 
dat= np.array([90,85,76,93])
s=pd.Series(dat, index=['A','B','C'])
dat={'A':90,'B':88,'C':76,'D':93}
s=pd.Series(dat, index=list(dat.keys()))

print(s['A'])
print(s.loc['A'])
print(s.iloc[0])

tot=np.sum(s)
m=np.mean(s)
ds=np.std(s)
print(s.describe())#resumen estadistico 
s.loc['E']=45
d={'F':15,'G':56,'H':62}
s2=pd.Series(d, index=list(d.keys()))
s3=pd.concat((5,52), axis=0)
"""Tenemos dos series o dos conjuntos de tuplas de datos distintas como las concateno ?
Hacia abajo o Hacia la derecha
ENtonces concatenamos con direccion en filas  
QUeda como resultado en la terminal: 
'A' 90 
B
C
D
'F' 15 ETC ETC
Si usamos axis=1 Se concatena por columnas 
"""
dat={'Nombre':['Ana','Pedro','Luis','Juan'],'Edad':[22,20,32,18]}
df=pd.DataFrame(dat, index=[100,101,102,103])
print(df)
df.iloc[102]["Edad"]#32

d={'c1':pd.Series([1,2,3], index=['a','b','c']),
   'c2':pd.Series([1,2,3,4], index=['a','b','c','d'])
   }
de=pd.DataFrame(d)
print(df)
"""va a imprimir c1 y c2 como tuplas una alado de la otra 
y c1 c2
a 1 1 
b 2 2 
c 3 3
'd nan 4"""


"""Maretes 18 de Noviembre 2025"""
dat={'uno':[1,2,3,4], 'dos';[4,3,,2,1]}
df=pd.DataFrame(dat, index=['a','b','c','d'])
print(df)
df['tres']=df['uno']*df['dos']
df['cuatro']=df['uno']>2
print(df)

df['extra']='ABC'
df['mejora']=df['one']*df[:2]

del df['cuatro']
tres= df.pop('tres')#pop retorna las columna
print(df,'\n', tres)
df.insert(1,'tres', df['one'])
df.pop('tres')
df.inserte(1,'tres,[1,2,3,4]')
print(df)

"""
Seleccionar por columna   df[columna]---  series
Seleccionar por etiqueta  df.loc[etiqueta] --serie
Seleecionar por indice   df.iloc[entero] --- serie 
Seleccionar filas con slicing   df[:5]--- Dataframe
Seleccionar filas con booleanos   df[exp]-- Dtataframe
retormnara un dataframe de ture o falses 



se agregan 2 columans nuebvas 
"""
df.columns=['c1','c2','c3','c4','c5']
df[[True, False, False, True, False]]

"""EXPRESIONES REGULARES 
Una expresion regular o 'regex' es una forma de reconocer y extraer datos a 
partir del reconocimiento de patrones textuales.
Una regex es una cadena donde cientos de caractes llamados 'metacaracteres'
tienen un significado especial, los cuales permitesns englobar una gran 
variedad de caracteres y expresiones textuales.
Por ejemplo:

"""
import re #pip install re 
exp=re.compile("hola")#cuantos holas hay?2 y si le pones Hola solo habra uno por la H mayuscula 
cuenta= 0
texto ="hola mundo y hola a todos \n".split(',')
for linea in texto:
    if exp.search(linea):
        cuenta+=1
print(cuenta) #2

exp=re.compile("hola or hola")
exp=re.compile(("h or H")ola)
exp=re.compile(["h or H"]ola)

exp=re.compile('[a-z]')
exp=re.compile('[0-9]')
exp=re.compile("[a-z, 0.9]")
exp=re.compile('[-0-9 ,a-z]')
"""exppresion para encontrar cualquie rnumero exadem"""

exp=re.compile('[0-9 a-fA-F]')




