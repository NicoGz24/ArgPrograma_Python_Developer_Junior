#Pedir un número por pantalla y decir si está entre 10 y 15 o no.

num = int(input('Ingrese un numero '))

if(num > 9 ) and (num < 16):
    print('El numero ingresado se encuentra dentro del rango')
else: print ('El numero ingresado esta fuera del rango')