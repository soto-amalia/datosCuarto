import random
def mayor(lista):
    mayor=lista[0]
    for numero in lista:
        if numero>mayor:
            mayor=numero
    return mayor
numeros=[2,5,8,9,1]
print(mayor(numeros))

def triangulo(tamano):
    for fila in range(1,tamano+1):
        print("*"*fila)
triangulo(10)
#triangulo equilatero

def triangulo2(tamano):
    for fila in range(1,tamano+1):
        espacios=(tamano-fila)//2
        figura=''
        if random.random()>0.2:
            figura +="O"
        else:
            figura+="*"

        print(" "*espacios+figura*fila)
triangulo2(20)
