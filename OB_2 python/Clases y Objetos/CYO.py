class Juguete:
    _encendido = True

    def enciende(self):
        self._encendido = True

    def apaga(self):
        self._encendido = False

    def isEncendido(self):
        return self._encendido


class Potato(Juguete):
    def quitarOreja(self):
        pass

    def ponerOreja(self):
        pass

class Dino(Juguete):
    def verEscamas(self):
        pass

p = Potato()
p.enciende()
print(p.isEncendido())
p.apaga()
print(p.isEncendido())




