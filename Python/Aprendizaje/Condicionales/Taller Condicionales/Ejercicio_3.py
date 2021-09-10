# Programa que determina si un número de 3 cifras es igual al derecho y al revés.

# Solicitud del número
x = input("Ingrese un número de 3 cifras: ")

# Comprobación
if x[0]==x[2]:
    print("El número ", x, " es igual al derecho y al revés")
else:
    print("El número ", x," no es igual al derecho y al revés")

# Créditos
print("====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================")
