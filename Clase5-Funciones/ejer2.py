#Idem al ejercicio anterior pero el carácter debe ser ingresado por teclado.

def dibujarRectangulo():
    car = input('Ingrese el caracter con el que quiere que se dibuje el rectangulo ')
    altura = int(input('Ingrese la altura del rectangulo '))
    anchura = int(input('Ingrese la anchura del rectangulo '))
    for i in range(anchura -1):
        print(car,end='')
    print(car)
    for i in range(altura):
        print(car,end="")
        for k in range(anchura):
            if(k == anchura -1):
                print(car)
            else:print(" ",end='')
    for i in range(anchura):
        print(car,end='')

dibujarRectangulo()
