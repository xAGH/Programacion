# Programa para solicitar el nombre y la edad,
#luego imprimirlos: el nombre en mayus inicial
#y a la edad sumarle 5
nombre=input("Escriba su nombre: ")
edad=input("Ingrese su edad: ")
#Convierto nombre con mayus inicial
nombre=nombre.title()
#Imprimo resultado
print("Bienvenido " + nombre)
print("Su edad es de: ", edad)
#Edad en 5 años
print(nombre,", su edad en 5 años es de: ", int(edad)+5)