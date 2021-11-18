# Programa que informa los valores pares e impares de distintos números ingresados

# Declaracíon de datos
veces=int(input(("Ingrese los números que desea verificar: ")))
i=0
impar=0
par=0
print("Ingrese los números: ")
while i<veces:
    numero=int(input()) 
    if numero%2==1:
        impar+=1
    else:
        par+=1
    i+=1
print("\nSe presentaron", par,"números pares y", impar,"números impares")

# Créditos
print("\n====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================\n")

    