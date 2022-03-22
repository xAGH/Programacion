# Clase con un atributo y un método privado.
# class encapsulamiento:
#     __privado_atri = "Soy un atributo que no se puede ver fuera de la clase."

#     def __privado_met(self):
#         print("Soy un metodo     que no se puede ver fuera de la clase.")

# e = encapsulamiento()

# Estas dos sentecnias devuelven un error debido a que el método y el atributo en cuestión, son "privados" y son elementos los cuales no se pueden acceder fuera de la clase.
# e.__privado_met()
# e.__privado_met()

# Clase con un atributo y un método privado, dando la posibilidad de acceder a ellos fuera de la clase.
class encapsulamiento:
    __privado_atri = "Soy un atributo que no se puede ver fuera de la clase."

    def __privado_met(self):
        print("Soy un metodo que no se puede ver fuera de la clase.")

    def publico_atri(self):
        return self.__privado_atri

    def publico_met(self):
        return self.__privado_met( )

e = encapsulamiento()
print(e.publico_atri())
print(e.publico_met())