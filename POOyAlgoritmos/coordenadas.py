class Coordenada:

# Atributos
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Métodos
    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5

# Uso
if __name__ == '__main__':
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    print(f'La distancia entre las dos coordenadas es: {coord_1.distancia(coord_2)}')

# Verificar si una instancia pertenece a una clase
    print(isinstance(coord_2, Coordenada))