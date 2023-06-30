# Definir una tupla llamada “letras” con las primeras 6 letras del abecedario (en minúscula) 
# por separado, es decir, cada letra es un elemento . Luego:

# ▪ Mostrar todos los elementos

# ▪ Mostrar todos los elementos del 2do al ultimo

# ▪ Mostrar todos los elementos del 1ro al 4to

# ▪ Mostrar todos los elementos del 3ro al 5to

# ▪ “Modificar” la tupla y cambiar las letras de minúsculas a mayúsculas

# ▪ Comprobar si existe en la tupla la letra con la que comienza tu nombre

# ▪ Determinar la cantidad de elementos de la tupla con la función len()

# ▪ Definir otra tupla “letras2” con las próximas 3 letras (en minúsculas)

# ▪ Unir “letras” y “letras2” en una sola tupla llamada “letras3”

# Mostrar las 3 tuplas por pantalla

letras = ('a','b','c','d','e','f')

# ▪ Mostrar todos los elementos
print(letras)

# ▪ Mostrar todos los elementos del 2do al ultimo
for i in range(2,len(letras)):
    print(letras[i])

print('--------------CORTE------------')
# ▪ Mostrar todos los elementos del 1ro al 4to
for i in range(0,4):
    print(letras[i])

print('--------------CORTE------------')
# ▪ Mostrar todos los elementos del 3ro al 5to
for i in range(3,5):
    print(letras[i])

print('--------------CORTE------------')
# ▪ “Modificar” la tupla y cambiar las letras de minúsculas a mayúsculas
lista = list(letras)
for i in range(len(lista)-1):
    lista[i] = lista[i].upper()
letras = tuple(lista)
print(letras)

print('--------------CORTE------------')
# ▪ Comprobar si existe en la tupla la letra con la que comienza tu nombre
encontre = letras.count('N')
if(encontre > 0):
    print('La tupla contiene la letra N')
else: print('La tupla no contiene la letra N')

print('--------------CORTE------------')
# ▪ Determinar la cantidad de elementos de la tupla con la función len()
print(f'La cantidad de elementos de la tupla es de {len(letras)}')

print('--------------CORTE------------')
# ▪ Definir otra tupla “letras2” con las próximas 3 letras (en minúsculas)
letras2 = letras + ('g','h','i')
print(letras2)

print('--------------CORTE------------')
# ▪ Unir “letras” y “letras2” en una sola tupla llamada “letras3”
letras3 = letras + letras2
print(letras3)

print('--------------CORTE------------')
# Mostrar las 3 tuplas por pantalla
print(f'Tupla 1 {letras}')
print(f'Tupla 2 {letras2}')
print(f'Tupla 3 {letras3}')