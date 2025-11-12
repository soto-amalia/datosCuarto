#BIBLIOTECA PARA ESTRUCTURAR DATOS 
#pip install numpy 
"""
-Los arreglos en numpy representan vectores/matrices con elementos del mismo tipo
de dato, indexados por una tupla de enteros no negativos.
-La dimencion del arreglo se denomina 'rango'
-La 'forma' es una tupla de enteros no negativos que representan el tamaño de cada dimension.

"""
import numpy as np
a=np.array([1,2,3])  #[1,2,3]
type(a)# class np.array
print(a.shape)#(3,)
print(a[0],a[1],a[2])
a[0]=5
print(a)#[5,2,3]

b=np.array([1,2,3],[4,5,6])#2 dimensiones
#en python para acceder al 2 b[0][1]
print(b.shape)#(2,3)
print(b[0],b[0,1])#[1,2,3]
np.zeros((2,2))
np.ones((2,2))
np.full((2,2),2) #matriz 2x2 con el numero 2
np.eye(2)#matriz identidad de 2x2 
np.random.random((2,2))#matriz de numeros random decimales 
"""excel se puede trabjar con visualexit
todo lo de algebra lineal s epude hacer con mumpy

"""
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b=a[0:2,1:3]
a[-2: ,-2,-4]
b=a.copy() #distinto b=a
print(a[0,1])#2
b[0,0]#7
print(a[0,1])#7,3 y 

r1=a[1, :]
r2=a[1:2, :]
print(r1.shape)
print(r1.shape)#(4,)
r1[1] #6
r2[0,1]
c1=[:2,1]

