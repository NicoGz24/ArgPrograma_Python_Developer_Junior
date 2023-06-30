# Ingresar valores numéricos por teclado e ir guardándolos en una lista. 
# El final del ingreso de números esta dado por el ingreso de un número negativo. 
# Se pide luego: 
# a) Mostrar los números pares de la lista (si no se ingreso ninguno, mostrar un cartel) 
# b) El máximo valor de los números guardados en la lista

lista=[]
num = int(input('Ingrese un numero '))
while(num >= 0):
    lista.append(num) 
    num = int(input('Ingrese un numero '))
max=-1
num = 0
for i in lista:
    if(i > max):
        max = i
    if(i % 2 == 0):
        print(i)
        num+=1
if(num == 0):
    print('No se ingresaron numeros pares')
if(max == -1):
    print(f'La lista se encuentra vacia')
else: 
    print(f'El numero mas grande que se ingreso fue el: {max}')