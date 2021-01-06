import random
import time

def busqueda_lineal(lista, objetivo, iter_lin=0):
    match = False
    #iteracion = 0
    for elemento in lista: #O(n)
        iter_lin += 1
        if elemento == objetivo:
            match = True
            break

    return (match, iter_lin)

def busqueda_binaria(lista, comienzo, final, objetivo, iter_bin=0):
    iter_bin +=1
    if comienzo > final:
        return (False, iter_bin)
    
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return (True, iter_bin)
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, iter_bin = iter_bin)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, iter_bin = iter_bin)

if __name__ == '__main__':
    
    tamano_de_lista = int(input('De qué tamaño será la lista? '))
    objetivo = int(input('Qué número quieres encontrar en la lista? '))


    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    (encontrado, iter_lin) = busqueda_lineal(lista, objetivo)
    (encontrado, iter_bin) = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"SI está :) " if encontrado else "NO está :( "} en la lista !!')
    print(f'El número total de iteraciones en la BÚSQUEDA LÍNEAL fue: {iter_lin}.')
    print(f'El número total de iteraciones en la BÚSQUEDA BINARIA fue: {iter_bin}.')