# Programa que muestra en pantalla una tabla de multiplicar ciertas veces.

# Declaración de variables
tabla=int(input("\nIngrese el número del cual desea saber su tabla de multiplicar: "))
veces=int(input("Ingrese el número de veces que se va a realizar la tabla de multiplicar: "))
i=1

# Resultados

while i<=veces:
    print("Vez #",i,":")
    print("\n1 : ",tabla*1)
    print("2 : ",tabla*2)
    print("3 : ",tabla*3)
    print("4 : ",tabla*4)
    print("5 : ",tabla*5)
    print("6 : ",tabla*6)
    print("7 : ",tabla*7)
    print("8 : ",tabla*8)
    print("9 : ",tabla*9)
    print("10: ",tabla*10, "\n")
    i+=1

# Créditos
print("====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================\n")
