class Persona:

    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        print('Camina!')

class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Monta en bicicleta!')

def main():
    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista('Daniel')
    ciclista.avanza()

if __name__ == '__main__':
    main()