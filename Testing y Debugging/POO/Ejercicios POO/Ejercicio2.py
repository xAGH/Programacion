"""Escribir una clase en python que calcule pow(x, n)

x = es la base

n = es el exponente
"""

class Pow_Calculator:

    def datos(self, x, n):
        self.n = n
        self.x = x

    def operar(self):
        self.resultado_pow = self.x ** self.n
    

    def resultado(self):
        print(f"El resultado de la potencia de {self.x} a la {self.n} es {self.resultado_pow}")

potencia = Pow_Calculator()
potencia.datos(2,2)
potencia.operar()
potencia.resultado()