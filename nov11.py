#BIBLIOTECA PARA ESTRUCTURAR DATOS 
#pip install numpy 

slacing
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
"""""
Miercoles 12 de Nov 2025
POdemso filtrar arreglos haciendo 
"""
a=np.array([1,2],[3,4],[5,6])#(2,3)2 dimensiones 
print(a[[0,1],[1,0]])#[2,3]
print(np.array([a[0,1],a[1,0]]))#[2,3]

print(a[[0,2,1],
        [0,0,1]])

ind=(a>2)
#ind=[false false
#     true true
#     true true ]todo como matriz 
print(a[ind])
#2 arreglos 
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])

print(a+b)
print(np.add(a,b))

print(a-b)
print(np.subtract(a,b))
print(a*b)
print(np.multiply(a,b))
print(a/b)
print(np.divide(a,b))
print(a**0.5)
print(np.sqrt(a))

x=np.array([9,10])#producto punto de estos numeros
=x.shape---> (2,)
y=np.array([11,12])#Va a multiplicar como en lineal [1234][910]=[9+20 27+40]=[29 77]

print(x.dot(y))#219
print(np.dopt(a,x))#[19 22 43 50 ]

print(a.dot(b))
np.matmul()#aab 

z=np.array([x])#(1,2)meteloa una variable y daler .shape debe de dar 1.2 
#como le hacemos para que de 2,1

z=np.array([x]).T #va a hacer la transpuesta osea una matriz de (2,1)

np.reashape(x,(2,1))#va a modificar la forma de la mastriz pero tu le indicas como exactamente
np.hstack(x)#vector fila
np.vstack(x)#vector columna

z=np.reshape(y, (1,2))
print(np.vstack(x).dot(z))
#



