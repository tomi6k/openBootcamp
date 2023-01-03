class Humano():
    def __init__(self, edad, altura, peso):
        self.edad = edad
        self.altura = altura
        self.peso = peso

    def Mostrar(self,):
        print("Tengo ", self.edad, " años. Mido ", self.altura, "mts  y peso ", self.peso," kgs")

d = Humano()

d.Mostrar("18","1.90","76")

