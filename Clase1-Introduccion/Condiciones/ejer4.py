'''
Definir como constantes MAX y MIN con valores de 50 y 25 respectivamente. 
Luego, ingresar una temperatura temp por teclado y decir:
hace calor ( cuando es igual o superior a 50 temp>=50)
está templado cuando es mayor o igual a 25 y menor que 50.
hace frio si es menor a 25.
'''
max = 50
min = 25
temp = float(input('Ingrese la temperatura '))

if(temp >= 50):
    print('Hace calor')
elif (temp >= 25) and (temp < 50):
    print('Esta templado')
else:
    print('Hace frio')