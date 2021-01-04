class Humano:
# Atributos
    def __init__(self, edad, genero):
        self.edad = edad
        self.genero = genero

# Métodos
    def hablar(self, mensaje):
        print (mensaje)

# Uso
if __name__ == '__main__':
    pedro = Humano(26, 'Hombre')
    maria = Humano(21, 'Mujer')

    print ('- Hola Maria soy Pedro soy', pedro.genero, 'y tengo', pedro.edad,'años de edad.')
    print ('- Hola Pedro soy Maria soy', maria.genero, 'y tengo', maria.edad,'años de edad.')

    pedro.hablar('- Maria que gusto.')
    maria.hablar('- El gusto es mío Pedro.')