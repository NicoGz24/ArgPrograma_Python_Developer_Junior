# Se tiene el siguiente diccionario:

# ordinales = {1:"Primero", 2:"Segundo", 3:"Tercero", 4:"Cuarto"}

# Escribir un programa que permita en primer lugar agregar una nueva clave al diccionario ordinales. Tanto la clave como el valor a agregar, serán solicitados al usuario del programa.

# En segundo lugar, se mostrará el diccionario y se solicitará al usuario el ingreso de una de las claves para borrarla. El método pop puede resultarle útil.

# Finalmente, se muestra el resultado sobre el diccionario ordinales.

ordinales = {1:"Primero", 2:"Segundo", 3:"Tercero", 4:"Cuarto"}

#atento a que el enunciado no aclara el tipo que se ingresara por teclado, se presupone que se seguiran ingresando del tipo int para la clave y del tipo string para los valores, al igual que lo que ya contiene el diccionario


# Escribir un programa que permita en primer lugar agregar una nueva clave al diccionario ordinales. Tanto la clave como el valor a agregar, serán solicitados al usuario del programa.
clave = int(input('Ingrese su nueva clave '))
valor = input('Ingrese el valor deseado ')
if(clave in ordinales):
    ok = input('La clave ingresada ya existe, esta seguro que desea reemplazar su valor ? -  Ingrese S/N ')
    if(ok.upper() == 'S'):ordinales[clave] = valor
else:
    ordinales[clave] = valor

print('-------------ESPACIO--------------')

# En segundo lugar, se mostrará el diccionario y se solicitará al usuario el ingreso de una de las claves para borrarla. El método pop puede resultarle útil.
print(ordinales)
clave = int(input('Ingrese la clave que desea borrar '))
if(clave in ordinales):
    ordinales.pop(clave)
    print('Clave borrarda')
else: print('La clave que se intenta borrar no se encuentra en el diccionario')
print('-------------ESPACIO--------------')

# Finalmente, se muestra el resultado sobre el diccionario ordinales.
print(ordinales)
