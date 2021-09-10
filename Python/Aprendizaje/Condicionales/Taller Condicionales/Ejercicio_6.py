# Programa que determina la cantidad de dinero que recibe un trabajador respecto a las horas extras trabajadas. 

# Solicitud y definición de datos
horas_trabajo=int(input("Ingrese las horas que ha trabajado: "))
pago_hora=int(input("Indique cuánto le pagan por hora: "))
pago_base=pago_hora*horas_trabajo
horas_extra=0

# Pago sin horas extra
if horas_trabajo<=48:
    pago=horas_trabajo * pago_hora

# Pago con horas extra
else:
    horas_extra=horas_trabajo-48

# Pago con 8 horas extra o menos
if horas_extra<=8:
    pago=pago_hora * 2 * horas_extra + pago_base

# Pago con 9 horas extra o más
elif horas_extra>8:
    pago_menos8=pago_hora * 16
    pago=pago_hora*3*(horas_extra-8)+pago_base+pago_menos8

# Resultado pago
print("Su pago total es de $", pago,", ya que trabajó ", horas_extra, " horas extra")

# Créditos
print("====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================")




    