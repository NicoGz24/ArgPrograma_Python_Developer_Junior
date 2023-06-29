#calcula e imprime el producto de la serie 2x4x6x8x … x20.

prod = 1

for i in range(2,21,2):
    prod = prod * i
    print(i)

print(f'El producto de la serie es {prod}')