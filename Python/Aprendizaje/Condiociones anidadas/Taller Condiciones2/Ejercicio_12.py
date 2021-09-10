# Programa que de acuerdo a los años de antigüedad y el sueldo, decide ciertas acciones o no.

# Declaración  de variables
nombre=input("Ingrese su nombre: ")
sueldo=int(input("Ingrese su sueldo actual: "))
antiguedad=int(input("Ingrese los años que tiene de antigüedad: "))

# Verificaciones
if sueldo<0 or antiguedad<0:
    print("\nNo puede ingresar datos negativos.")
else:
    if sueldo<1000000 and antiguedad>=10:
        aumento=sueldo*0.2
        sueldo=sueldo+aumento
        print("\n",nombre,", su nuevo sueldo es de $",sueldo)  
    elif sueldo<1000000 and antiguedad<10:
        aumento=sueldo*0.05
        sueldo=sueldo+aumento
        print("\n",nombre,", su nuevo sueldo es de $",sueldo) 
    elif sueldo>=1000000:
        print("\n",nombre, ",su saldo es de $", sueldo)
    else:
        print("Hubo un problema, inténtelo de nuevo.")
        
# Créditos
print("\n====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================\n")
