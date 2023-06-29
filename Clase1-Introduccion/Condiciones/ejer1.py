#Pedir tres números por teclado e imprimir el mayor de ellos solamente.
num1 = int(input('Ingrese el primer numero '))
num2 = int(input('Ingrese el segundo numero '))
num3 = int(input('Ingrese el tercer numero '))
if (num1 > num2) and (num1 > num3):
    max = num1
elif (num2 > num3):
    max = num2
else:
    max = num3

print(f'El mayor de los numeros ingresados es el {max}')