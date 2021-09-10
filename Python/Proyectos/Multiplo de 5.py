numero = int(input("Ingrese un número para verificar si es múltiplo de 5: "))
operacion = numero % 5
if operacion == 0:
    respuesta = "es"
else: 
    respuesta = "no es"
    
print(f"El número {numero} {respuesta} múltiplo de 5")