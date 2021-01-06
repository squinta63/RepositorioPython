import random
import time

def busqueda_lineal(lista, objetivo, iteracion=0):
    match = False
    #iteracion = 0
    for elemento in lista: #O(n)
        iteracion += 1
        if elemento == objetivo:
            match = True
            break

    return (match, iteracion)
    

if __name__ == '__main__':
    
    tamano_de_lista = int(input('De qué tamaño será la lista? '))
    objetivo = int(input('Qué número quieres encontrar en la lista? '))
    
    tiempo_inicial = time.time()

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    (encontrado, iteracion) = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"SI está :) " if encontrado else "NO está :( "} en la lista !!')
    print(f'El número total de iteraciones fue: {iteracion}.')
    print(f'El tiempo total de ejecución fue de {time.time() - tiempo_inicial} segundos.')