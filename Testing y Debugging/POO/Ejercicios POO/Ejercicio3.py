"""Realizar un programa en el cual se declaren dos valores enteros 
por teclado utilizando el método __init__. Calcular después la suma, 
resta, multiplicación y división. Utilizar un método para cada una e imprimir 
los resultados obtenidos. Llamar a la clase Calculadora."""

class Calculadora():
    
    def __init__(self):
        while True:
            try:
                self.valor1 = float(input("Ingrese el valor 1: "))
                self.valor2 = float(input("Ingrese el valor 2: "))
                break

            except:
                print("Error en el ingreso de datos, ingrese solo números enteros o decimales, si es decimal, separe la parte decimal de la enmtra con un punto(.)")

    def suma(self):
        self.nombre = 'Suma'
        self.resultado = self.valor1 + self.valor2

    def resta(self):
        self.nombre = 'Resta'
        self.resultado = self.valor1 - self.valor2

    def multiplicacion(self):
        self.nombre = 'Multiplicación'
        self.resultado = self.valor1 * self.valor2

    def division(self):
        self.nombre = 'División'
        self.resultado = self.valor1 / self.valor2

    def imprimir_resultado(self):
        print(f"El resultado de la operación {self.nombre} es {self.resultado}")


datos = Calculadora()
datos.suma()
datos.imprimir_resultado()
datos.resta()
datos.imprimir_resultado()
datos.multiplicacion()
datos.imprimir_resultado()
datos.division()
datos.imprimir_resultado()