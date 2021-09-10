# Programa que convierte kg a unidades de medaida de masa.

# Decisión de ejercicio y declaración de variables. 
kg=int(input("Ingrese la cantidad de kg a convertir y la medida a la cual desea hacer la conversión: \nCantidad de kg: "))
ejercicio=input("""Unidad de medida: \n1. Hectogramos\n2. Decagramos\n3. Gramos\n4. Decigramos
5. Centígramos\n6. Miligramos\n7. Todos\nUnidad: """)

# Conversion
hectogramos=kg*10
decagramos=kg*100
gramos=kg*1000
decigramos=kg*10000
centigramos=kg*100000
miligramos=kg*1000000

# Elección d eejercicio y respuesta
if ejercicio=="1" or ejercicio.title()=="Hectogramos":
    print(kg,"kg equivalen a",hectogramos,"hectogramos")
elif ejercicio=="2" or ejercicio.title()=="Decagramos":
    print(kg,"kg equivalen a",decagramos,"decagramos")
elif ejercicio=="3" or ejercicio.title()=="Gramos":
    print(kg,"kg equivalen a",gramos,"gramos")
elif ejercicio=="4" or ejercicio.title()=="Decigramos":
    print(kg,"kg equivalen a",decigramos,"decigramos")
elif ejercicio=="5" or ejercicio.title()=="Centigramos":
    print(kg,"kg equivalen a",centigramos,"centigramos")
elif ejercicio=="6" or ejercicio.title()=="Miligramos":
    print(kg,"kg equivalen a",miligramos,"miligramos")
elif ejercicio=="7" or ejercicio.title()=="Todos":
    print("\n",kg,"kg equivalen a:\n",hectogramos,"hectogramos\n",decagramos,"decagramos\n",gramos,"gramos\n",decigramos,"decigramos\n",centigramos,"centigramos\n",miligramos,"miligramos")
else:
    print("Ingresó un dato no válido")

# Créditos
print("\n====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================\n")
