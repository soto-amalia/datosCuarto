frase=input("Dame una frase ")
#contar el no de caracttotaleres
total=len(frase)
print('El numero de caracteres de tu texto es:'+str(total))
#contar caracteres sin espacios 

total_sin_espacios=total-frase.count(' ')
print(str(total_sin_espacios))