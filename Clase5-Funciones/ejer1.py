#Escriba un programa que por medio de una función pida la anchura y altura de un rectángulo y lo dibuje con caracteres producto (*).


def dibujarRectangulo():
    altura = int(input('Ingrese la altura del rectangulo '))
    anchura = int(input('Ingrese la anchura del rectangulo '))
    for i in range(anchura -1):
        print('*',end='')
    print('*')
    for i in range(altura):
        print('*',end="")
        for k in range(anchura):
            if(k == anchura -1):
                print("*")
            else:print(" ",end='')
    for i in range(anchura):
        print('*',end='')

dibujarRectangulo()
