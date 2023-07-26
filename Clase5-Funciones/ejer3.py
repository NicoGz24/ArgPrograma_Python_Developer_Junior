# Escriba un programa que permita que una función reciba una lista de valores (que puede ser vacía). 
# El programa tiene que pedir un número y luego solicitar ese número de valores para crear la lista. 
# Luego, a traves de otra función devolver al programa principal la lista y el mayor y menor valor de la misma


def mayorMenor(lista):
    num = int(input('Ingrese un numero '))
    for i in range(num):
        val = int(input('Ingrese un valor numerico '))
        lista.append(val)
    return lista, max(lista), min(lista)

lista = []
lista,max,min = mayorMenor(lista)
print(lista)
print(f'El elemento mayor es {max}')
print(f'El elemento menor es {min}')