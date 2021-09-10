# Programa que determina cuánto debe pagar un cliente por el estacionamiento de su vehículo

# Solicitud de tiempo
horas=int(input("Indique el tiempo que ha estado su vehículo estacionado\nHoras: "))
minutos=int(input("Minutos(1-59): "))

# Validación que los minutos sean mayores de 0 y menores de 60, cálculo de pago
if minutos>0 and minutos<60:
    horas=horas+1
    pago=horas*1500
    # Resultado
    print("Su vehículo ha estado estacionado por", horas, "horas, debe pagar $", pago)

# Validación que las horas o los minutos no sean negativos
elif minutos<0 or horas<0:
    print("No se admiten números negativos")

# Respuesta por si las horas y los minutos son 0 
elif minutos==0 and horas==0:
    print("No debe pagar nada por 0 horas y 0 minutos")

else:
    print("Si son mas de 60 minutos, planteese expresarlo como 1 hora")

# Créditos
print("====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================")
