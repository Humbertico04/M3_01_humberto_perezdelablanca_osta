"""Creación
Copia el ejercicio anterior y realicemos una modificación:

Junto al método init y calificacion, vamos a crear otro método especial de Python, el método str. 
Al igual que init, debe ir encerrado entre dobles guiones bajos, y debe tener el siguiente formato:

def __str__(self): return "Lo que quiero mostrar"

Este método nos sirve para imprimir por pantalla la información de un objeto, 
si tenemos un objeto alumno1 creado y realizamos print(alumno1), 
Python ejecutará el contenido del método str (el método str lo que tiene que hacer es maquetar la información que desea en un string).

Experimentación
Implementa el método str y haz que muestre el nombre y la nota del alumno
Crea algun objeto de la clase Alumno
Realiza print de esos objetos para visualizar por pantalla la información del st"""

class Alumno:
    """Creamos la clase Alumno que recoge la nota y el nombre del alumno"""
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def calificacion(self):
        """Muestra si el alumno ha aprobado o a suspendido"""
        if self.nota >= 5:
            print("{} ha sacado un {} y ha aprobado \n".format(self.nombre, self.nota))
        else: 
            print("{} ha sacado un {} y ha suspendido \n".format(self.nombre, self.nota))

    def __str__(self): 
        """Muestra la información del objeto"""
        return "Nombre: {} \nNota: {}".format(self.nombre, self.nota)

#Experimentamos con algunos alumnos
Juan = Alumno("Juan", 10)
print(Juan)
Juan.calificacion()

Luis = Alumno("Luis", 3)
print(Luis)
Luis.calificacion()

Sofia = Alumno("Sofia", 5)
print(Sofia)
Sofia.calificacion()