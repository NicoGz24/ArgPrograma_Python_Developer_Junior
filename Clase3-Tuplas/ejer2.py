# Definir la tupla “números” con los siguientes números enteros:

# ▪ 7, 5, 2, 3, 4, 8, 6, 9, 2

# Buscar y mostrar por pantalla el máximo valor y su posición en la lista utilizando max() e index(). 
# ¿Qué sucede si quiero hacer lo mismo para obtener el menor valor y su ubicación? 
# Contar y mostrar por pantalla la cantidad de veces que aparece el numero 2 con count()

numeros = (7, 5, 2, 3, 4, 8, 6, 9, 2)
print (f'El máximo valor de la listas es el {max(numeros)} y su posición en la lista es {(numeros.index(max(numeros)))+1}')