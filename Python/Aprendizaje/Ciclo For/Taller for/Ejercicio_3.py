# Programa que dice de acuerdo a n números, cual es mayor, menor y diferencia entre ellos

veces=int(input("Determine la cantidad de números a ingresar: "))
mayor=0
menor=0
print(f"Ingrese los {veces} numeros.")
for i in range(1,veces+1):
    numero=int(input(f"Numero #{i}:"))
    if i==1:
        mayor=numero
        menor=numero
    elif numero>mayor:
        mayor=numero
    elif numero<menor:
        menor=numero
diferencia=mayor-menor
print(f"El mayor es: {mayor}\nEl menor es: {menor}\nLa diferencia es: {diferencia}")

# Créditos
print("\n====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================\n")
