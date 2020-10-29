import time

def run():
    def enumeracion(objetivo):
        respuesta = 0

        while respuesta**2 < objetivo:
            print(respuesta)
            respuesta += 1
        if respuesta**2 == objetivo:
            print(f'La raiz cuadrada de {objetivo} es {respuesta}')
        else:
            print(f'{objetivo} no tien una raiz cuadrada exacta')
    
    def aproximacion(objetivo, epsilon):
        tiempo_inicial = time.time()

        paso = epsilon ** 2
        respuesta = 0.0

        while abs(respuesta ** 2 - objetivo) >= epsilon and respuesta <= objetivo:
            print(abs(respuesta ** 2 - objetivo), respuesta)
            respuesta += paso
        
        if abs(respuesta ** 2 - objetivo) >= epsilon:
            print(f'No se encontró la raíz cuadrada de {objetivo}')
        else:
            print(f'La raíz cuadrada de {objetivo} es {respuesta}')

        print(f'El tiempo total de ejecución fue de {time.time() - tiempo_inicial} segundos')

    def busqueda_binaria(objetivo, epsilon):
        tiempo_inicial = time.time()
        
        limite_inferior = 0.0
        limite_superior = max(1.0, objetivo)
        respuesta = (limite_inferior + limite_superior) / 2

        while abs(respuesta ** 2 - objetivo) >= epsilon:
            print(f'limite_inferior={limite_inferior}, limite_superior={limite_superior}, respuesta={respuesta}')
            if respuesta ** 2 < objetivo:
                limite_inferior = respuesta
            else:
                limite_superior = respuesta

            respuesta = (limite_inferior + limite_superior) / 2
        
        print(f'La raíz cuadrada de {objetivo} es {respuesta}')
        print(f'El tiempo total de ejecución fue de {time.time() - tiempo_inicial} segundos')

    menu = """
    Bienvenido a la calculadora de raíces cuadradas
    1 - Método enumeración
    2 - Método aproximación
    3 - Método búsqueda binaria
    Elige una opción: """

    opcion = int(input(menu))

    if opcion == 1:
        objetivo = int(input('Escoge un entero: '))
        enumeracion(objetivo)
    elif opcion == 2:
        objetivo = int(input('Escoge un número: '))
        epsilon = float(input('Escoge un épsilon: '))
        aproximacion(objetivo, epsilon)
    elif opcion == 3:
        objetivo = int(input('Escoge un número: '))
        epsilon = float(input('Escoge un épsilon: '))
        busqueda_binaria(objetivo, epsilon)
    else:
        print ("Debes elegir una opción correcta!!😢")

if __name__ == '__main__':
    run()