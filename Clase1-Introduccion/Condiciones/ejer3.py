#Pedir lado y alto de un cuadrilátero y decir si es cuadrado o rectángulo.
lado = float(input("Ingrese la longitud del lado del cuadrilátero: "))
alto = float(input("Ingrese la altura del cuadrilátero: "))

if lado == alto:
    print("Es un cuadrado.")
else:
    print("Es un rectángulo.")