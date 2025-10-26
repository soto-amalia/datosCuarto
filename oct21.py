"""""
DATOS ESTRUCTURADOS Y SEMIESTRUCTURADOS
Comma_Separated Values(CSV)
En este formato los datos se presentan como registros 
-Los campos estan delimitados por comas (,)
-Los registros estas delimitados por saltos de lines (\n)
Todos los registros deben tener el mismo número de campos 
EJEMPLOS: 
Daniel , Cardenas, 34
"Daniel" , "Cardenas", 34
"Daniel" , "Cardenas López", "34"
"Daniel" , "Cardenas", 34, "Gustavo A. Madero "GAM", CDMX"
No se diferencía ente encabezados y los datos Nombre, Apellidos, Edad--->HEADER 
Daniel, Cardenas, 34
Podemos usar pandas para leer un CSV: 

"""
import pandas as pd
df=pd.read.CSV("datos.csv")
print(df.head())#5 primeros registros 
print(df.tail())#5 ultimos registros 
#Para leer columnas y filas específicas: 
df=pd.read_csv("datos.csv", nrows=4, usecols=[1,2,4])#userows=[1,3,4]
print(df)
df.fo_csv("archivo")#--> escribir dataframe a "archivo"

"""""Hierarchical Data Format (HDF)
Es un formato de código abierto diseñado para alcanzar datos de estructura 
compleja y de tamaño considerable  
HDF5 tiene dos componentes principales: 
-GRUPOS:Similares a carpetas. Pueden contener datasets u otros grupos.
-DATASETS:Son archivos binarios que contienen a los datos y su estructura. 
Se suelen alojar en grupos.




"""""
