#¿Sabrías hacer que Python te diga cuántas repeticiones del valor 10 hay en esta lista? 
#lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]

lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]
cant = 0
for i in lista_numeros:
    if(i == 10):
        cant+=1
print(f'La cantidad de veces que aparece el numero 10 es {cant}')
 