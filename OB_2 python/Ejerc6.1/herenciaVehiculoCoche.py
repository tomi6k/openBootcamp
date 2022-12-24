class Vehiculo():
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.puertas = puertas
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, ruedas {}, puertas {}".format(self.color, self.ruedas, self.puertas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas,)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + '{} km/h, {} cc' .format(self.cilindrada, self.velocidad)

ford = Coche('rojo', 4,5,190,1200)
volkswagen = Coche('gris',4,3,220,1600)

print(ford)
print(volkswagen)