# Se define la clase Auto
class Auto:
    rojo = False

    # Método __init__ o constructor, instancia el objeto al momento de ser llamada la clase.
    def __init__(self, puertas=None, color=None):
        self.puertas = puertas
        self.color = color
        if puertas != None and color != None:
            print(f"Se creó un auto con {puertas} puertas y de color {color}.")

        else:
            print("Se creó un auto sin especificar su número de puertas ni su color")

    def Fabricar(self):
        self.rojo = True
    
    def confirmar_fabricacion(self):
        if (self.rojo):
            print("El auto es rojo.")

        else:
            print("EL auto no es rojo.")

# Se crea el objeto
a = Auto()
a2 = Auto(4, "Rojo")