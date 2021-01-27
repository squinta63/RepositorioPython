import random

def media(X):
    return sum(X) / len(X)

def varianza(X):
    mu = media(X)

    acumulador = 0
    for x in X:
        acumulador += (x - mu)**2
    
    return acumulador / len(X)

def desviacion_estandar(X):
    return (varianza(X))**0.5


if __name__ == '__main__':
    X = [random.randint(1, 21) for i in range(20)]
    mu = media(X)
    Var = varianza(X)
    sigma = desviacion_estandar(X)

    print(f'Datos: {X}')
    print(f'Media = {mu}')
    print(f'Varianza = {Var}')
    print(f'Desviación estandar = {sigma}')