# Añade a la lista colores = ["rojo", "azul", "verde", "amarillo"] los siguientes colores en los sitios donde se te pide. 
# Lo tienes que hacer con algún método de adición de elementos, no puedes editar la lista manualmente. 
# Tienes que añadir los colores en el código en este orden:
# gris – Antes de «rojo».

# rosa – En último lugar.

# naranja – Entre «azul» y «verde».

lista_colores = ["rojo", "azul", "verde", "amarillo"] 
lista_colores.insert(0,"gris")
lista_colores.append("rosa")
lista_colores.insert(3,"naranja")
print(lista_colores)