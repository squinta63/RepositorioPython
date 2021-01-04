# Clase 1 **********
class Automovil:
# Atributos
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        # Atributos privados (Variable interna) con el _ después del punto
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros=4)

# Métodos
    def acelerar(self, tipo='despacio'):
        if tipo == 'rapido':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
        
        self._estado = 'en_movimiento'

    def frenar(self):
        self._estado = 'en_reposo'
    
    def girar(self, giro: str):
        if giro == "derecha":
            print(f'Girando a la {giro}')
        else:
            print(f'Girando a la {giro}')
    
    def informacion(self):
        print(f'El vehículo de color: {self.color}, marca: {self.marca}, modelo: {self.modelo}.')

# Clase 2 **********
class Motor:
# Atributos
    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

# Métodos  
    def inyecta_gasolina(self, cantidad):
        pass

# Uso

if __name__ == '__main__':
    auto_sebas = Automovil(2014, 'KIA', 'GRIS')
    auto_sebas.informacion()

