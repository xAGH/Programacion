class Fabrica:
    def __init__(self, marca, nombre, precio, descripcion, ruedas=None, distribuidor=None):
        self.marca = marca
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.ruedas = ruedas
        self.distribuidor = distribuidor

    def __str__(self):
        return f"""
        MARCA\t\t{self.marca}
        NOMBRE\t\t{self.nombre}
        PRECIO\t\t{self.precio}
        DESCRIPCION\t{self.descripcion}
        RUEDAS\t\t{self.ruedas}
        DISTRIBUIDOR\t{self.distribuidor}
        """

Carro = Fabrica('Ford', 'Ranger', 10000000, 'Camioneta 4x4', 4)

print(str(Carro))

class Auto(Fabrica):
    pass

z = Auto("Ferrari", "Veneno", 100000000, "Auto deportivo")

print(z)

class Deportivo(Fabrica):
    
    ruedas = ""
    distribuidor = ""

    def __str__(self):
        return f"""\
MARCA\t\t{self.marca}
NOMBRE\t\t{self.nombre}
PRECIO\t\t{self.precio}
DESCRIPCION\t{self.descripcion}
RUEDAS\t\t{self.ruedas}
DISTRIBUIDOR\t{self.distribuidor}     
"""

deportivo = Deportivo('Volkswagen', 'Vento', 54000, 'EL mejor, el mas veloz')
deportivo.ruedas = 6
deportivo.distribuidor = "Alejin"

print(deportivo)