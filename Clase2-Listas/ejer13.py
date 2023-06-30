# Defina la siguiente lista: [1,4,4,5,9,4,6,4,8,7,3,4]. 
# Escriba un código que cuente la cantidad de veces que se repite un número ingresado por teclado.

lista = [1,4,4,5,9,4,6,4,8,7,3,4]
num = int(input('Ingrese el numero a buscar '))
cant=0
if (num in lista):
    for i in lista:
        if(i == num):
            cant+=1
print(f'La cantidad de veces que aparecio el numero {num} en la lista fue de {cant}')
