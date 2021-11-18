"""Crear un programa con tres clases Universidad, con atributos nombre
(Donde se almacena el nombre de la Universidad). Otra llamada Carerra,
con los atributos especialidad (En donde me guarda la especialidad de un estudiante).
Una ultima llamada Estudiante, que tenga como atributos su nombre y edad.
El programa debe imprimir la especialidad, edad, nombre y universidad de dicho
estudiante con un objeto llamado persona."""

class Universidad():

    def nombreUni(self):
        nombre = input("Ingrese el nombre de la Universidad: ")
        self.nombreU = nombre

    def __str__(self):
        return self.nombreU


class Carrera():

    def especialidadEs(self):
        especialidad  = input("Ingrese la especialidad del estudiante: ")
        self.especialidad = especialidad

    def __str__(self):
        return self.especialidadE

class Estudiante(Universidad, Carrera):

    def datosE(self):
        nombre = input("Ingrese su nombre como estudiante: ")
        edad = input("Ingrese su edad: ")
        self.nombreE = nombre
        self.edad = edad

    def imprimir(self):
        print(f"""\n
Nombre de la Universidad:\t{self.nombreU}
Carrera del Estudiante:\t\t{self.especialidad}
Nombre del Estudiante:\t\t{self.nombreE}
Edad del Estudiante:\t\t{self.edad}
""")

persona = Estudiante()
persona.nombreUni()
persona. especialidadEs()
persona.datosE()
persona.imprimir()