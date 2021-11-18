# Programa que verfiica si 3 números ingresados son negativos o no

# Declaración de variables
n1=int(input("Ingrese tres números.\nNúmero #1: "))
n2=int(input("Número #2: "))
n3=int(input("Número #3: "))

# Validación y respuesta
if n1<0 and n2<0 and n3<0:
    print("\nTodos los números son menores a 0")
else:
    print("\nNo todos los números son negativos")

# Créditos
print("\n====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================\n")
