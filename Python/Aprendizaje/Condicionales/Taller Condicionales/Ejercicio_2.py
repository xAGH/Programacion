# Programa que solicita un número e imprime si es par o impar y positivo o negativo

#Solicitud del número
numero=int(input("Ingrese un número entero: "))

# Cálculo y definición de si el número es par o impar
modulo=numero%2
if modulo==0:
    modulo="par"
else: 
    modulo="impar"

# Definición de si el número es positivo o negativo
if numero>=0:
    valor="positivo"
else: 
    valor="negativo"

# Resultado
print("El número ", numero, " es ", modulo, " y es ", valor)

# Créditos
print("====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================")

