#Pedir peso y altura para calcular la masa corporal: mc = peso / altura^2.

peso = float(input('Ingese el peso '))
altura = float(input('Ingrese la altura '))
mc = peso/altura**2
print(f'La masas corporal en base al peso y altura ingresado es {mc}')