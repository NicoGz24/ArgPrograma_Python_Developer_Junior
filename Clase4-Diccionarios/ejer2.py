# Definir un diccionario con 4 elementos. Las claves son clave1, clave2, clave3 y clave4. 
# Y los valores correspondientes a cada clave son: un valor entero, un valor booleano, un string y una lista que contiene los números desde el 1 al 4.
# a) Mostrar a que tipo corresponde la estructura completa.

# b) Mostrar cada uno de sus valores usando sus claves

# c) Mostrar que tipo de dato tiene cada valor de clave

# d) Agregar un elemento más al diccionario

# e) Ingresar por teclado un dato y determinar si existe una clave que coincida con alguna clave del diccionario. Si se encuentra mostrar el valor asociado

# f) Copiar en forma “superficial” el diccionario y modificar el primer valor de clave. Observar que sucede con el diccionario original Poner el valor cero a todos los valores del diccionario

# g)Recorrer y mostrar todos los elementos clave-valor del diccionario Ingresar por teclado un dato y eliminar del diccionario dicho dato si se encuentra dentro del diccionario.

# h)Eliminar todos los elementos del diccionario

dic = {'clave1':24,'clave2':True,'clave3':'pedro','clave4':[1,2,3,4]}
print(dic)
print('-------------ESPACIO--------------')

# a) Mostrar a que tipo corresponde la estructura completa.
print(type(dic))
print('-------------ESPACIO--------------')

# b) Mostrar cada uno de sus valores usando sus claves
print(dic['clave1'])
print(dic['clave2'])
print(dic['clave3'])
print(dic['clave4'])
print('-------------ESPACIO--------------')

# c) Mostrar que tipo de dato tiene cada valor de clave
print(type(dic['clave1']))
print(type(dic['clave2']))
print(type(dic['clave3']))
print(type(dic['clave4']))
print('-------------ESPACIO--------------')

# d) Agregar un elemento más al diccionario
dic['clave5'] = ('hola','silla')
print(dic)
print('-------------ESPACIO--------------')

# e) Ingresar por teclado un dato y determinar si existe una clave que coincida con alguna clave del diccionario. Si se encuentra mostrar el valor asociado

#valor = input('Ingrese el valor a buscar ')
valor = 'clave2'
if(valor in dic):
    print(dic[valor])
else:print('El valor ingresado no se encuentra en el diccionario')
print('-------------ESPACIO--------------')

# f) Copiar en forma “superficial” el diccionario y modificar el primer valor de clave. Observar que sucede con el diccionario original Poner el valor cero a todos los valores del diccionario
dic2 = dic.copy()
dic2['clave1'] = 'valorNuevo'
print(dic2)
print(dic)
print('-------------ESPACIO--------------')


# g)Recorrer y mostrar todos los elementos clave-valor del diccionario Ingresar por teclado un dato y eliminar del diccionario dicho dato si se encuentra dentro del diccionario.
for i in dic:
    print(f'Clave {i} - Valor: {dic[i]}')

valor = input('Ingrese el dato a borrar ')
if(valor in dic):
    dic.pop(valor)
    print(dic)
else:print('El valor no se encuentra en el diccionario')
print('-------------ESPACIO--------------')

# h)Eliminar todos los elementos del diccionario
dic.clear()
print(dic)