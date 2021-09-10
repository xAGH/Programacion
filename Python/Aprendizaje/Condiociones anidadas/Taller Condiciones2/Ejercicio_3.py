# Programa que determina un resultado según la edad de la persona

# Declaración de variables
edad=int(input("Ingrese una edad: "))

# Validaciones
if edad<1:
    print("\nLa edad no puede ser un valor menor que 1")
elif edad>120:
    print("\nLa edad mo puede ser un valor mayor que 120")
else:
    if edad>18:
        print("\nSi tiene permiso de acceso")
    else:
        print("\nNo tiene permiso de acceso")

# Créditos
print("====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================")
