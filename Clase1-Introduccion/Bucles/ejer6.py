#Implementar un código que, ingresando 20 números, encuentre y devuelva el mayor de ellos.

max = -1

for i in range(20):
    num = int (input('Ingrese un numero '))
    if(num > max):
        max = num
print(f'El numero mas grande ingresado es el {max}')