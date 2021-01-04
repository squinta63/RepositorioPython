class Persona:
# Atributos 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Métodos
    def saluda(self, otra_persona):
        return (f'Hola {otra_persona.nombre}, me llamo {self.nombre}')

# Uso
if __name__ == '__main__':
    david = Persona('David', 35)
    erika = Persona('Erika', 32)
    print(david.saluda(erika))