# Programa que lee los lados de n triangulos e informa el tipo de triángulo y la cantidad de tringulos de cada tipo

veces=int(input("¿Cuántos triángulos va a ingresar?\nTriángulos:  "))
equilatero=0
isoceles=0
escaleno=0
print("Ingrese el valor de cada lado del triángulo: ")

for i in range(1,veces+1):
    lado1=int(input("Lado 1: "))
    lado2=int(input("Lado 2: "))
    lado3=int(input("Lado 3: "))

    if lado1==lado2 and lado2==lado3:
        print(f"El triángulo #{i} es un triángulo equilátero\n")
        equilatero=equilatero+1

    elif lado1==lado2 or lado1==lado3 or lado2==lado3:
        print(f"El triángulo #{i} es un triángulo isóceles\n")
        isoceles=isoceles+1
    
    else:
        print(f"El triángulo #{i} es un triángulo escaleno\n")
        escaleno=escaleno+1

if equilatero>0:
    print(f"\nLa cantidad de triángulos equilateros son: {equilatero}")
if isoceles>0:
    print(f"\nLa cantidad de triángulos isoceles son: {isoceles}")
if escaleno>0:
    print(f"\nLa cantidad de triángulos escaleno son: {escaleno}")

# Créditos
print("\n====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================\n")


