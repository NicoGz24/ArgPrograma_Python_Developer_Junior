#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
palabra = input('Ingrese una palabra ')

reverso = palabra[::-1]

if(palabra == reverso):
    print('La palabra ingresada es un palindromo')
else:
    print('La palabra ingresada NO es un palindromo')