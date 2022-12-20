peso = float(input("Ingrese su peso en KG: "))
altura = float(input("Ingrese su altura en MT: "))

alturaCuad = altura * altura

imc = peso / float(alturaCuad)

print("Su indice de masa corporal es: ", round(imc,2))

