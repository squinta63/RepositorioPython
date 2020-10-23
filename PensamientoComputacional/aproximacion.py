import time

def run():
    tiempo_inicial = time.time()
    objetivo = int(input('Escoge un número: '))
    epsilon = 0.01
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

if __name__ == "__main__":
    run()