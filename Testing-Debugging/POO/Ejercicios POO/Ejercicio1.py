"""Realizar un programa que conste de una clase llamada Alumno 
que tenga como atributos el nombre y la nota del alumno. Definir 
los métodos para inicializar sus atributos, imprimirlos y mostrar 
un mensaje con el resultado de la nota y si ha aprobado o no."""

class Alumno:

    def datos(self, nombre_alumno=None, nota_alumno=None):
        self.nombre = nombre_alumno
        self.nota = nota_alumno

    def resultado(self):
        estado = "aprobado" if self.nota > 5 else "reprobado"
        self.resultado = f"{self.nombre} ha {estado}"

    def imprimir(self):
        print(self.resultado)
        

alumno1 = Alumno()
alumno1.datos("ALejo", 8)
alumno1.resultado() 
alumno1.imprimir()

alumno2 = Alumno()
alumno2.datos("Carlos", 4)
alumno2.resultado()
alumno2.imprimir()