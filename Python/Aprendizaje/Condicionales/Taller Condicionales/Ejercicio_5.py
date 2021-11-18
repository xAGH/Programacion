# Programa que calcula las calorias que consume el cuerpo d eun enfermo dependiendo la actividad que esté haciendo

# Solicitud de datos
actividad=input("Ingrese la actividad que está realizando el paciente(relacione con un número):\n1. Durmiendo\n2. Sentado\n3. En reposo\nRespuesta: ")
tiempo_m=int(input("Ingrese el tiempo que ha estado el paciente haciendo dicha actividad\nMinutos: "))
tiempo_h=int(input("Horas: "))
tiempo_total=tiempo_h*60 + tiempo_m 

# Validación de datos
if int(actividad)<0 or int(actividad)>3:
    print("Ingrese un número del 1 al 3")

# Verificación y determinación de datos
elif actividad=="1":
    calorias=1.08*tiempo_total
    print("El cuerpo del paciente ha consumido ", round(calorias,2))

elif actividad=="2" or actividad=="3":
    calorias=1.66*tiempo_total
    print("El cuerpo del paciente ha consumido ", round(calorias,2))

# Créditos
print("====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================")

