#De la lista resultante del ejercicio anterior, elimina los valores «rojo», «verde» y «amarillo» con el método pop().

lista_colores = ["rojo", "azul", "verde", "amarillo"] 
lista_colores.insert(0,"gris")
lista_colores.append("rosa")
lista_colores.insert(3,"naranja")
print(lista_colores)

lista_colores.pop(1)
lista_colores.pop(3)
lista_colores.pop(3)
print(lista_colores)