# Programa que pide un número del 1 al 7 y dice el dia de la semana correspondiente

# Declaración de variables
numero=int(input("Ingrese un número del 1 al 7: "))

# Validación
if numero<0 or numero>7:
    print("Ingresó un valor fuera de los parámetros.")

# Respuesta
else:
    if numero==1:
        dia="lunes"
    elif numero==2:
        dia="martes"
    elif numero==3:
        dia="miércoles"
    elif numero==4:
        dia="jueves"
    elif numero==5:
        dia="viernes"
    elif numero==6:
        dia="sábado"
    elif numero==7:
        dia="domingo"
    print("Segun el número ingresado, el dia correspodiente es el",dia)
    
# Créditos
print("\n====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================\n")
