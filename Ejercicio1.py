class Alumno:
    """Creamos la clase Alumno que recoge la nota y el nombre del alumno"""
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("El alumno {} se ha creado con éxito".format(nombre))
    
    def calificacion(self):
        """Muestra si el alumno ha aprobado o a suspendido"""
        if self.nota >= 5:
            print("{} ha sacado un {} y ha aprobado \n".format(self.nombre, self.nota))
        else: 
            print("{} ha sacado un {} y ha suspendido \n".format(self.nombre, self.nota))


#Experimentamos con algunos alumnos
Juan = Alumno("Juan", 10)
Juan.calificacion()

Luis = Alumno("Luis", 3)
Luis.calificacion()

Sofia = Alumno("Sofia", 5)
Sofia.calificacion()

