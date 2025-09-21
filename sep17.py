#Hacer una funcion que cheque si un numero es primo o no 
#Un número primo es un número natural mayor que 1 que solo tiene dos divisores exactos: el 1 y él mismo. Por ejemplo, el 5 es un número primo porque solo se puede dividir entre 1 y 5. Los números con más de dos divisores se llaman números compuestos (como el 6, que es divisible entre 1, 2, 3 y 6), mientras que el 1 no es primo ni compuesto porque tiene solo un divisor. 

"""""def primo(numero):
    ###Devuelve True si es primo, False si no lo es.
    
    if numero <= 1:
        return False  # 0, 1 y negativos no son primos

    for divisor in range(2, int(numero**0.5) + 1):
        if numero % divisor == 0:
            return False  # tiene un divisor distinto de 1 y él mismo
    return True


# Ejemplo de uso
n = int(input("Dame un número: "))

if primo(n):
    print(f"{n} SÍ es primo ")
else:
    print(f"{n} NO es primo ")
""""""""""

#
# # Es necesario que retorne true y false 

def primo(n):
    if n==1:
        return print("No es primo")
    if n==2:
        return print("Es rpimo")
    if n%2==0:
        return print("no es primo")
    for i in range(3,n,2) #n//2
        if n%i==0:
                return print("Es primo")
    return print("Es primo ")


""""""""""""""""
inicio=[]
for n in range(10):
     if primo(n):
     inicio.append(n)
print(inicio)
""""""""""



""""""""""""""""""""""
inicio=[n for n in range(10)
        if primo(n)]
"""""""""""""


""""""""""""""""""""""""
tu le metes un elemento a la funcion y le plica la funcion a cada elemento del iterable
inicio=list(map(primo(n), range(10)))
""""""""""""""""""""


""""""""""""""""""""""""
tu le metes un elemento a la funcion y le plica la funcion a cada elemento del iterable
inicio=list(map(primo, range(10)))
#[true, false]
""""""""""""""""""""



""""""""""""""""""""""""
filter me va a regresar los valores que son verdaderos y lo que son falsos  
inicio=list(filter(primo, range(10)))
""""""""""""""""""""

#investigar que es tuple and did