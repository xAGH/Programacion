# EL cliente solicita un programa que diga que número de los dos ingresados es el mayor.

print("Ingrese dos números: ")
num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))

if num1 > num2:
    print(f"El número 1({num1}) es mayor.")

elif num2 > num1:
    print(f"El número 2({num2}) es mayor.")

else:
    print("Los números son iguales.")