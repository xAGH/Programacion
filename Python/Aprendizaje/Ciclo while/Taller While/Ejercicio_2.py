# Programa que pregunta por x edades y de acuerdo a estas, muestra un promedio.

# Declaracíon de datos
print("Ingrese las edades de las personas (digite 0 para salir): ")
i=0
edad=""
suma=0
while edad!=0:
    edad=int(input())
    if edad<=0:
        print("Saliendo del ciclo")
    else:
        i+=1
        suma=edad+suma
print("El promedio de las edades es: ",round(suma/i,2))

# Créditos
print("\n====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================\n")

    