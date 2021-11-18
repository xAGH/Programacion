"""Escribir una clase que se llame Areas().
A partir de un constructor se deben pasar 
los valores de Base y Altura. Luego, se debe 
calcular area de un cuadrado, triangulo y pentagono"""

from math import tan

class Areas:

    def __init__(self):
        while True:
            try:
                self.base = float(input("Ingrese el valor de la base: "))
                self.altura = float(input("Ingrese el valor de la altura: "))
                self.lados = int(input("Ingrese el número de lados del polígono regular: "))
                break

            except:
                print("Error en el ingreso de datos, ingrese solo números enteros o decimales, si es decimal, separe la parte decimal de la enmtra con un punto(.)")

    def area_cuadrado(self):
        self.nombre = "Cuadrado"
        self.area = self.base * self.altura

    def area_triangulo(self):
        self.nombre = "Triángulo"
        self.area = (self.base * self.altura) / 2

    def area_poligono(self):
        self.nombre = "Polígono regular"
        angulo = 360 / self.lados
        apotema = (self.base) / (2*tan(angulo / 2))
        perimetro = self.base * self.lados
        self.area = (perimetro * apotema) / 2

    def imprimir(self):
        print(f"El área de {self.nombre} es {self.area}")

datos = Areas()

datos.area_cuadrado()
datos.imprimir()

datos.area_triangulo()
datos.imprimir()

datos.area_poligono()
datos.imprimir()