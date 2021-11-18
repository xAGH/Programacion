"""Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio;
luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro.
Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes.
Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno"""

class Fabrica():

    def __init__(self, Llantas, Color, Precio):
        self.llantas = Llantas
        self.color = Color
        self.precio = Precio
        

class Moto(Fabrica):

    def __str__(self):
        return f"Se creó la moto de color {self.color} con {self.llantas} ruedas y con un precio de {self.precio}"

class Carro(Fabrica):
    
    def __str__(self):
        return f"Se creó el carro de color {self.color} con {self.llantas} ruedas y con un precio de {self.precio}"

moto = Moto(2, "Rojo", '$3.000.000')
carro = Carro(4, "Azul", '$30.000.000')

print(str(moto))
print(str(carro))