"""Programa que solicita dos numeros, los compara entre si y si el primero es mayor que el segundo
los numeros se sumaran y restaran. Si el segundo numero
es mayor que el primero, estos se multiplicaran y dividir"""

n1=int(input("Ingrese el número 1: "))
n2=int(input("Ingrese el número 2: "))
if n1>n2:
    print("El primer número es mayor que el segundo, por lo tanto: ")
    print("La suma de los números es: ", n1+n2)
    print("La resta de los números es: ",n1-n2)
elif n2>n1:
    print("El segundo número es mayor que el primero, por lo tanto: ")
    print("La multiplicación de los números es: ", n1*n2)
    print("La división de los números es: ", n1/n2)
else:
    print("Los números son iguales")
