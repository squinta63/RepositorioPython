def run():
    def divide_elementos_de_lista(lista, divisor):
        try:
            return [i / divisor for i in lista]
        except ZeroDivisionError as e:
            print(e)
            return lista

    lista = list(range(10))
    divisor = 

    print(divide_elementos_de_lista(lista, divisor))


if __name__ == '__main__':
    run()