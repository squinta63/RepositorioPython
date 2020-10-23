import time
def run():
    tiempo_inicial = time.time()
    objetivo = int(input('Escoge un número: '))
    epsilon = 0.001
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


if __name__ == "__main__":
    run()