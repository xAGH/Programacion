# Programa que pide tres números y verifica si la suma de los dos primeros son igual al tercero

# Declración de variables
n1=int(input("Ingrese tres números.\nNúmero #1: "))
n2=int(input("Número #2: "))
n3=int(input("Número #3: "))

n1_n2=n1+n2

# Determinación e impresión del resultado
if n3==n1_n2:
    print("\nLa suma de los dos primeros números es igual al tercero\n")
else:
    print("\nLa suma de los dos primeros números no es igual al tercero\n")

# Créditos
print("====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================\n")
