# Programa que solicita 3 números,los muestra en pantalla de mayor a menor en lineas distintas.
# En caso de haber numeros iguales, se pintan en la misma linea.

# Solicitud de datos 
n1=int(input("Ingrese tres números.\nNúmero #1: "))
n2=int(input("Número #2: "))
n3=int(input("Número #3: "))

# En caso de que no se presenten números iguales
if n1>n2 and n2>n3:
    print("\nEl orden de los números es:\n",n1,"\n",n2,"\n",n3,"\n")

elif n1>n3 and n3>n2:
    print("\nEl orden de los números es:\n",n1,"\n",n3,"\n",n2,"\n")

elif n2>n3 and n3>n1:
    print("\nEl orden de los números es:\n",n2,"\n",n3,"\n",n1,"\n")

elif n2>n1 and n1>n3:
    print("\nEl orden de los números es:\n",n2,"\n",n1,"\n",n3,"\n")

elif n3>n2 and n2>n1:
    print("\nEl orden de los números es:\n",n3,"\n",n2,"\n",n1,"\n")

elif n3>n1 and n1>n2:
    print("\nEl orden de los números es:\n",n3,"\n",n1,"\n",n2,"\n")

# En caso de que se pressenten números iguales
elif n1==n2 and n3<n1:
    print("\nEl orden de los números es:\n",n1,"=",n2,"\n",n3,"\n")
elif n1==n2 and n3>n1:
    print("\nEl orden de los números es:\n",n3,"\n",n1,"=",n2,"\n")

elif n1==n3 and n2<n1:
    print("\nEl orden de los números es:\n",n3,"=",n1,"\n",n2,"\n")
elif n1==n3 and n2>n1:
    print("\nEl orden de los números es:\n",n2,"\n",n1,"=",n3,"\n")

elif n2==n3 and n1<n2:
    print("\nEl orden de los números es:\n",n2,"=",n3,"\n",n1,"\n")
elif n1==n2 and n1>n2:
    print("\nEl orden de los números es:\n",n1,"\n",n2,"=",n3,"\n")

# En caso de que los 3 números sean iguales
elif n1==n2 and n2==n3:
    print("\nLos tres números son iguales\n")

# Créditos
print("====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================\n")
