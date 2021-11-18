# Programa que pida letra y detecte si es una vocal.

# Solicitud de datos
letra=input("Ingrese una letra: ")

# Validación
if len(letra)>1:
    print("Ingresó una palabra, solo se admiten letras individualmente")

# Comprobación
else:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print("La letra ", letra, " es una vocal")
    else:
        print("La letra ", letra, " no es una vocal")

# Créditos
print("====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================")
