import random
import collections

PINTAS = ['picas', 'corazones', 'diamantes', 'treboles']
VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k']

def crear_baraja():
    barajas = []
    for pinta in PINTAS:
        for valor in VALORES:
            barajas.append((valor, pinta))
    
    return barajas

def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)

    return mano

def main(tamano_mano, intentos):
    barajas = crear_baraja()
    
    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)
    
    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[0])
        
        counter = dict(collections.Counter(valores))
        for val in counter.values():
            if val == 2:
                pares += 1 
                break
        
    probabilidad_par = pares / intentos
    print(f'La probabilidad de obtener un par en una mano de {tamano_mano} cartas es: {probabilidad_par}')



if __name__ == '__main__':
    tamano_mano = int(input('¿De cuántas cartas quieres la mano?: '))
    intentos = int(input('¿Cuántos intentos para calcular la probabilidad?: '))
    
    main(tamano_mano, intentos)
