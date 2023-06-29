#Realizar un programa que permita adivinar un número. 
#Para ello se solicitara el ingreso por teclado del numero a adivinar (entero). 
#Luego se irán solicitando mas números y se deberá ir averiguando si el número a adivinar 
#es mayor o menor que el introducido (ir mostrando carteles indicativos). 
#El programa termina cuando se acierta el número.

num = int(input('Ingrese el numero secreto '))
encontrado = False

while (not encontrado):
    num2 = int(input('Ingrese su numero, probemos suerte '))
    if(num2 == num):
        encontrado = True
        print('Bien, adivinaste')
    elif (num2 > num):
        print('El numero ingresado es mayor al secreto')
    else: print('El numero ingresado es menor al numero secreto') 