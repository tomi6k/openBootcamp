class Alumnos():  # Clase Alumnos
    def info(self, nombre, nota):  # Se inicializan los atributos base 
        self.nombre = nombre
        self.nota = nota

    
    def imprimir(self):   # Metodo Imprimir
        print ("Nombre: ", self.nombre)  
        print ("Nota: ", self.nota)

    def resultado(self):   # Metodo que compara nota y dice si esta aprobado o no
        if self.nota < 5:
            print("Estas desaprobado")
        else :
            print("Estas aprobado")

alumno1 = Alumnos()  # Instancia alumno1
alumno2 = Alumnos()  # Instancia alumno2

alumno1.info("Juan",6)
alumno2.info("Lionel",10)

alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()
