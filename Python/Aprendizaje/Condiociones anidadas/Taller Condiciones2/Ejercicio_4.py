# Programa que pide 3 números y los muestra en pantalla de menor a mayor

# Solicitud de datos 
n1=int(input("Ingrese tres números.\nNúmero #1: "))
n2=int(input("Número #2: "))
n3=int(input("Número #3: "))

# Determinacion y exposición de los resultados
if n1>n2 and n2>n3:
    print("\nEl orden de los números es:\n",n3,"\n",n2,"\n",n1,"\n")

elif n1>n3 and n3>n2:
    print("\nEl orden de los números es:\n",n2,"\n",n3,"\n",n1,"\n")

elif n2>n3 and n3>n1:
    print("\nEl orden de los números es:\n",n1,"\n",n3,"\n",n2,"\n")

elif n2>n1 and n1>n3:
    print("\nEl orden de los números es:\n",n3,"\n",n1,"\n",n2,"\n")

elif n3>n2 and n2>n1:
    print("\nEl orden de los números es:\n",n1,"\n",n2,"\n",n3,"\n")

elif n3>n1 and n1>n2:
    print("\nEl orden de los números es:\n",n2,"\n",n1,"\n",n3,"\n")

elif n1==n2 or n1==n3 or n2==n3:
    print("\nDos o más números son iguales","\n")

# Créditos
print("====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================\n")
