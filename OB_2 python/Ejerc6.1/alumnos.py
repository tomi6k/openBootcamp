class Alumnos():
    def info(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    
    def imprimir(self):
        print ("Nombre: ", self.nombre)
        print ("Nota: ", self.nota)

    def resultado(self):
        if self.nota < 5:
            print("Estas desaprobado")
        else :
            print("Estas aprobado")

alumno1 = Alumnos()
alumno2 = Alumnos()

alumno1.info("Juan",6)
alumno2.info("Lionel",10)

alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()
