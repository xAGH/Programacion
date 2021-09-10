# Programa que verifica si una fecha ingresada es la fecha de la batalla de Boyacá

# Declaración de variables.
dia=int(input("Ingrese una fecha(Solo los números son válidos).\nDia: "))
mes=int(input("Mes: "))
año=int(input("Año: "))

# Validaciones
if dia<0 or mes<0 or año<0:
    print("Los datos no pueden ser negativos")
else:
    if dia>31 or mes>12:
        print("Los datos exceden los límites")
    else: 
        if dia==7 and  mes==7 and año==1819:
            print("La fecha ingresada coincide con la batalla de Boyacá")
        else:
            print("La fecha ingresada no coincide con la batalla de Boyacá") 

# Créditos
print("====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================\n")
