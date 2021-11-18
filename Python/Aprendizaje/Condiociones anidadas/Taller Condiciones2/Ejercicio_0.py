# Programa que determina si un número ingresado es positivo, negativo o cero

# Solicitud del número
x=int(input("Ingrese un número entero: "))

# Comprobaciones

if x<0:
    resultado=" negativo"
elif x>0:
    resultado=" positivo"
else: 
    resultado=" cero"
print("El número ingresado es ", resultado)

# Créditos
print("====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================")
