#Duplica esta lista en otra.
lista_colores = ["rojo", "azul", "verde", "amarillo"] 
lista_colores.insert(0,"gris")
lista_colores.append("rosa")
lista_colores.insert(3,"naranja")

lista_colores.pop(1)
lista_colores.pop(3)
lista_colores.pop(3)
print(lista_colores)

lista_aux = lista_colores
print(lista_aux)