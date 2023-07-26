# Sea el siguiente diccionario: s= {'fruta':' Peras', 'cantidad': 10, 'precio': 35.10)}
# Mostrar la fruta y la cantidad
# Mostrar el precio
# Modificar el precio por el valor de 75
# Agregar un par clave-valor con la fecha de compra
# Mostrar las claves del diccionario utilizando el for
# Mostrar el par clave-valor del diccionario
# Pasar el diccionario a una lista
# Eliminar un elemento del diccinario

s= {'fruta':' Peras', 'cantidad': 10, 'precio': 35.10}

#Mostrar la fruta y la cantidad

print(s['fruta'], s['cantidad'])

print('-------------ESPACIO--------------')

# Mostrar el precio

print(s['precio'])

print('-------------ESPACIO--------------')

s['precio'] = 75
print(s['precio'])

print('-------------ESPACIO--------------')

# Agregar un par clave-valor con la fecha de compra

s['fecha_compra'] = '23/06/2023'
print (s)

print('-------------ESPACIO--------------')

# Mostrar las claves del diccionario utilizando el for

for i in s:
    print(f'Clave {i}')

print('-------------ESPACIO--------------')

# Mostrar el par clave-valor del diccionario
for i in s:
    print(f'Clave: {i} - valor: {s[i]}')

print('-------------ESPACIO--------------')

# Pasar el diccionario a una lista
lista = list(s)
print(lista)

print('-------------ESPACIO--------------')
# Eliminar un elemento del diccinario
s.pop('fecha_compra')
print(s)