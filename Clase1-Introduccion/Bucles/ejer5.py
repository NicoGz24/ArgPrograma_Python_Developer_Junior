#Calcula e imprime la suma de la serie 50+48+46+ … +20.
sum = 0
for i in range(50, 19, -1):
    sum += i

print(f'La suma de la serie da como resultado {sum}')