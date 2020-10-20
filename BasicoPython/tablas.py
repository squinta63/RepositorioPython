menu = """
Bienvenido al programa de tablas de multiplicar
1 - Tabla del 1
2 - Tabla del 2
3 - Tabla del 3
4 - Tabla del 4
5 - Tabla del 5
6 - Tabla del 6
7 - Tabla del 7
8 - Tabla del 8
9 - Tabla del 9
Elige una opción: """
opcion = int(input(menu))

def producto(numero):
    for i in range(10):
        print(str(numero) + 'x' + str(i) + ' = ' + str(numero*i))

def run():
    if opcion == 1:
        producto(1)
    elif opcion == 2:
        producto(2)
    elif opcion == 3:
        producto(3)
    elif opcion == 4:
        producto(4)
    elif opcion == 5:
        producto(5)
    elif opcion == 6:
        producto(6)
    elif opcion == 7:
        producto(7)
    elif opcion == 8:
        producto(8)
    elif opcion == 9:
        producto(9)
    else:
        print('Elija una opción correcta!!')

    

if __name__ == '__main__':
    run()