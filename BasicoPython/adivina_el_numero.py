import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un número del 1 al 100: '))
    vidas = 10
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Debes elegir un número mayor!!')
            vidas -= 1
        else:
            print('Debes elegir un número mas pequeño!!')
            vidas -= 1
        if vidas == 0:
            print('Game Over!')
            break
        print('Tienes ' + str(vidas) + ' vidas')
        numero_elegido = int(input('Elige otro número: '))
        if numero_elegido == numero_aleatorio:
            print('¡Ganaste!')


if __name__ == '__main__':
    run()