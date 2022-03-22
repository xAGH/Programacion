class Fabrica:
    # Método __init__ o constructor, instancia el objeto al momento de ser llamada la clase.
    def __init__(self, tiempo, nombre, ruedas):
        self.tiempo = tiempo
        self.nombre = nombre
        self.ruedas = ruedas
        print(f"Se creó el auto {self.nombre}")

    # Método __del__ o deconstructor, instancia un objeto y elimina el anterior objeto definido con el mismo nombre.
    def __del__(self):
        print(f"Se eliminó el auto {self.nombre}")

    # Método que al ser llamado retorna un mensaje.
    def __str__(self):
        return f"{self.nombre} con {self.ruedas} ruedas se creó satisfactoriamente en {self.tiempo} minutos."

    # Método que al ser llamado retorna un valor entero de acuerdo al valor pasado en el método.
    def __len__(self):
        return self.tiempo
    


# Se instancia el objeto pasando los parámetros solicitados.
a = Fabrica(10,"Alejo", 2)

# Si se vuelve a instanciar un objeto con el mismo nombre, entra al método __del__ el cual eliminará el objeto intanciado anteriormente e instanciará un nuevo objeto con las especificaciones dadas.
# a = Fabrica(10,"Alejandro", 2)

# Se llama al método __str__ el cual nos muestra un mensaje.
print(str(a))

# Se llama al método __len__ el cual nos muestra el valor de un entero indicado.
print(len(a))