#Solicitar el ingreso de un número, el programa deberá indicar si el número ingresado es múltiplo de 7.

num = int(input('Ingrese un numero '))
if(num % 7 == 0):
    print('El numero ingresado es multiplo de 7')
else:
    print('El numero ingresado no es multiplo de 7')