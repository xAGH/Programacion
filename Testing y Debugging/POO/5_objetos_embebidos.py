class Fabrica:
    def __init__(self, tiempo, nombre, ruedas):
        self.tiempo = tiempo
        self.nombre = nombre
        self.ruedas = ruedas
        print(f"Se creó el auto {self.nombre}")

    def __str__(self):
        return f"{self.nombre}({self.tiempo})"

class Listado:
    
    def __init__(self, autos=[]):
        self.autos = autos

    def fabricar(self, x):
        self.autos.append(x)

    def visualizar(self):
        for elemento in self.autos:
            print(elemento)

a = Fabrica(10, "Alejo", 4)
l = Listado([a])
l.visualizar()
l.fabricar(Fabrica(5,"Michael", 2))
l.visualizar()