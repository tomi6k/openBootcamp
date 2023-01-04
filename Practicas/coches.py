class Coche():
    ruedas = 4

    def __init__(self, color, puertas, año):
        self.color = color
        self.puertas = puertas
        self.año = año

    # def ingresarDatos(self):
    #     self.color = str(input("Ingrese el color del Coche: "))
    #     self.puertas = int(input("Ingrese la cantidad de puertas: "))
    #     self.año = int(input("Ingrese año de su Coche: "))

    def mostrar(self):
        return "Su coche es color: ", self.color , " tiene ", self.puertas ," puertas y es del año " ,self.año

vehiculo = Coche("Rojo", 4, 2001)

# vehiculo.ingresarDatos()
vehiculo.mostrar("rojo", 4 , 2001)