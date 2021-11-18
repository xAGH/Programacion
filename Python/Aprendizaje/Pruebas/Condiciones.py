# Solicitar dos números por teclado, evaluar si el primero es mayor al segundo o si el segundo es menor al primero

#Solicito variables o datos

numero1=int(input("Ingrese el número 1: "))
numero2=int(input("Ingrese el numero 2: "))
if(numero1>numero2):
    print("El primer numero(", numero1,"), es el mayor")
elif(numero2>numero1): 
    print("El segundo numero(", numero2,"), es el mayor")
else:
    print("Los números son iguales")
print("================================================")
print("Programa realizado por Alejandro Giraldo Herrera")
