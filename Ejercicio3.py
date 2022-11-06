"""Creación
Crea una clase llamada Producto que tenga los atributos codigo, nombre, precio y tipo.
Crea el constructor de la clase. Añadir en el constructor un print para informar de que el producto se ha creado con éxito
Crea el método __str__ para visualizar por pantalla la información de los productos

Experimentación
Crea algunos productos
Prueba a mostrar los datos de algun producto y a modificar algun valor, por ejemplo, prueba a modificar el precio de un producto"""

from ast import main

print("Ejercicio 3:\n")

class Producto:
    """Creamos la clase producto"""
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        print("El producto se ha creado con éxito")

    def __str__(self):
        """Muestra la información del objeto"""
        return "{} con codigo de barras {} pertenece a {} y cuesta {}\n".format(self.nombre, self.codigo, self.tipo, self.precio)

#Experimentamos con algunos productos
producto1 = Producto("848042347", "La sandía", "9.80€", "frutería")
print(producto1)
producto2 = Producto("848094863", "La hamburguesa", "2.70€", "carnicería")
print(producto2)
producto3 = Producto("848068295", "Las oreo", "1.90€", "apretivos")
print(producto3)

if __name__=="__main__":
    main()