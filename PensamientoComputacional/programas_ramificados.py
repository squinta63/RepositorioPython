nombre_1 = input('Escribe el nombre número 1: ')
edad_1 = int(input('Cuál es la edad del nombre número 1: '))

nombre_2 = input('Escribe el nombre número 2: ')
edad_2 = int(input('Cuál es la edad del nombre número 2: '))

if edad_1 > edad_2:
    print(f'{nombre_1} es mayor que {nombre_2}')
elif edad_1 < edad_2:
    print(f'{nombre_2} es mayor que {nombre_1}')
else:
    print(f'{nombre_1} y {nombre_2} tienen la misma edad')
    
