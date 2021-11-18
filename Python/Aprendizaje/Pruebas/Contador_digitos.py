# Programa que lee un número positivo ingresado por el usuario y devuelve cuantos digitos tiene

n1=int(input("Ingrese un número positivo: "))
if n1>=0:
    print("El número ingresado tiene ", len(str(n1)), "dígitos")
else:
    print("El número debe de ser positivo")