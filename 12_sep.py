def fibonacci(numero):
    inicio=0
    siguiente=1
    if numero <1:
        print("error, las series de fibonacci solo pueden ser a partir de 1")
    else:
        for i in range(numero):
            # inicio,siguiente = siguiente,inicio+siguiente
            temp = siguiente   
            siguiente = inicio + siguiente
            inicio = temp   
            print(" el numero actual es ",inicio)
        return siguiente


num_usuario = int(input(("Dame un numero: ")))
print(fibonacci(4))
print("------")
print(fibonacci(num_usuario))







