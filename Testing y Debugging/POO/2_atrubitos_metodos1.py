# Se define la clase Auto
class Auto:
    rojo = False

    # Método __init__ o constructor, instancia el objeto al momento de ser llamada la clase.
    def __init__(self):
        print("Se creó un auto.")

    def Fabricar(self):
        self.rojo = True
    
    def confirmar_fabricacion(self):
        if (self.rojo):
            print("El auto es rojo.")

        else:
            print("EL auto no es rojo.")

# Se crea el objeto
a = Auto()

# Accedo al método confirmar_fabricacion() el cual verifica si el atrinuto rojo es True o False, en un inicio es False
a.confirmar_fabricacion()

# Aplico el método Fabricar al objeto a, el cual cambia rojo de False a True
a.Fabricar()

# Se vuelve a acceder al método confirmar_fabricacion(), el cual me devuelve True ya que se cambió el valor de este atributo al objeto con el método Fabricar()
a.confirmar_fabricacion()

