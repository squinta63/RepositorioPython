import random


def ordenamiento_insercion(lista):
    n = len(lista)

    for i in range(1, n):
        valor_actual = lista[i]
        for j in range(i, 0, -1):

            if valor_actual < lista[j-1]:
                lista[j-1], lista[j] = lista[j], lista[j-1]
    return lista

if __name__ == '__main__':
    tamano_de_lista = int(input('De qué tamaño será la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_insercion(lista)
    print(lista_ordenada)