# Escribir un programa que permita cargar las temperaturas del mes. 
# Luego debe recorrer la lista y calcular: 
# a) La temperatura promedio del mes. 
# b) La temperatura máxima y el día en que ocurrió 
# c) La temperatura mínima, y el día en que ocurrió 
# d) la cantidad de días con temperaturas mayores al promedio.

listaTemp = []

#se presupone que se carga una temperatura por dia

for i in range (10):
    temp = float(input('Ingrese la temperatura del dia de hoy '))
    listaTemp.append(temp)
#para hacerla mas corta solo cargo 10 dias
print('LISTA CARGADO')
prom = 0
max = -50
diaMax = 0
diaMin = 0
min = 555
for k in listaTemp:
    prom += k
    if (k > max):
        max = k
        diaMax = listaTemp.index(k)+1
    if(k < min):
        min = k
        diaMin = listaTemp.index(k)+1
prom = prom/len(listaTemp)
print('PRIMER ANALISIS TERMINADO')
dias = 0
for j in listaTemp:
    if (j > prom):
        dias+=1
print('SEGUNDO ANALISIS TERMINADO')
print(f'La temperatura promedio del mes fue de {prom}')
print(f'La temperatura máxima fue de {max} y el día en que ocurrió fue el {diaMax}')
print(f'La temperatura mínima fue de {min}, y el día en que ocurrió fue el {diaMin}')
print(f'La cantidad de días con temperaturas mayores al promedio fue de {dias}')