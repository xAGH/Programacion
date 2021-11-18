# Progrma que calcula el factorial de un número

factorial=1
numero=int(input("Ingrese el número a calcular el factorial: "))
if numero<0:
    print("El número no puede ser negativo")
elif numero>50000:
    print("El número es demasiado grande")
else:
    for i in range(1,numero+1):
        factorial=factorial*numero
        numero=numero-1
        cifras=len(str(factorial))
print(f"El factorial de {i} es: {factorial}")
print(f"El número tiene {cifras} cifras")

# Créditos
print("\n====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================\n")
