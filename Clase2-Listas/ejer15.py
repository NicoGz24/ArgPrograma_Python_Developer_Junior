#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

lista1 = [1,2,3]
lista2 = [-1,0,2]

sum = 0

for i in range(len(lista1)):
    sum += lista1[i]*lista2[i]
print(f'El producto escalar es {sum}')

