class Coche:
  def __init__(self):
    self.acelerado = False

  def acelerar(self):
    self.acelerado = True
    print("El coche está acelerando")

  def frenar(self):
    self.acelerado = False
    print("El coche está frenando")

# Crear una instancia de la clase Coche
coche1 = Coche()

# Comprobar si el coche está acelerado
print(coche1.acelerado)  # imprime False

# Acelerar el coche
coche1.acelerar()

# Comprobar si el coche está acelerado
print(coche1.acelerado)  # imprime True

# Frenar el coche
coche1.frenar()

# Comprobar si el coche está acelerado
print(coche1.acelerado)  # imprime False
