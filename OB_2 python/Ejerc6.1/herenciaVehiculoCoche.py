class Vehiculo():
    Color = "Rojo"
    Ruedas = "4"
    Puertas = "4"

class Coche(Vehiculo):
    Velocidad = 300
    Cilindrada = "1300cc"

p = Coche()

print("El coche tiene: ", p.Ruedas, " ruedas.")
print("Tambien tiene " , p.Puertas, " puertas")
print("Su color es: ", p.Color)
print("Su velocidad maxima es ",p.Velocidad, " con ", p.Cilindrada, " en su motor.")
