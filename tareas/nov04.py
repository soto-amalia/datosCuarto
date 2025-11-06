"""""
BASES DE DATOS NO RELACIONALES 
Las bases de datos "no relacinales " o NoSQL son estructuras que alamacenan datos en objetos
distintos a las tablas relacionales.
Algunas caracteristicas de estas bases son : 
-Estructura flexible
-Escalamiento horizontal
-COnsultas eficientes y rapidas 

Tipode de bases NoSQL:
-DOCUMENTOS:Almacenan datos en archivos similares a un JSON. Contienen un numero arbitrario de pares llave-valor.
-BASADOS EN COLUMNAS:Los datos se organizan por columnas en lugar de filas.
-BASADOS EN GRAFOS: Los datos se alamcenan en nodos y bordes.
    -Los nodos contienen loos daros de los objetos que describen.
    -Los bordes describen la naturaleza de las relaciones entre los nodos.
Tenemos 2 tablas: 
--USUARIO--
ID   NOMBRE    APELLIDO   CIUDAD 
1   YIRE        REYNA       CDMX
2   ISMAEL      RAMIREZ     CDMX
3   MARIA       HERNANDEZ    VERACRUZ
4   AMALIA      SOTO        EDO. MEX.

--PASATIEMPOS--
ID      ID_USUARIO      PASATIEMPO 
10      2       TIK TOK
11      1       PELICULAS
12      3       COCINAR
13      2       LEER
14      4       PROGRAMAR
15      1       VIAJAR
16      1       BAILAR

YIRE RAYNA--- JSON
{
    "ID":1
    "NOMBRE":"YIRE"
    "APELLIDO":"REYNA"
    "CIUDAD":"CDMX"
    "PASATIEMPOS":["PELICULAS","VIAJAR","BAILAR"]
}

MARIA DB, Y MONGO -- CONECTORES Docker
Contenedor: AMbientes aue estan prefabricados para cumplir por ej una conexion con mongo para correr todo para poder utilizarlo
Maquina virtual, ambiente separado de tu compu para hacer algo que no tenga nada que ver  se supone que no itneractua y la info es separada 
QUeber--- Administra contneedores 


"""

