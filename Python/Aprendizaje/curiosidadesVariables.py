# Con el sufijjo 'del' en una variable, borraremos ésta
a = 10
print(a)
# del a
print(a)

# Creacion de una tupla sin paréntesis:
tupla = 200,3,4,5,6,"Hola"
print(tupla)
 
# Tipo de dato numérico complex
x = complex()
print(x)

# Obtener un número binario
binario = bin(120) # Esto devuelve el número binario con un sufijo 0b, por esto mismo, tomamos la cadena desde la posición dos.
print(binario[2:])

# Obtener número octal
octal = oct(64) # Esto devuelve el número octal con un sufijo 0o, por eso mismo, tomamos la cadena desde la posición doos.
print(octal[2:])

# Obtener número hexadecimal
hexadecimal = hex(1600) # Esto devuelve el número hexadecimal con un sufijo 0x, por eso mismo, tomamos la cadena desde la posición doos.
print(hexadecimal[2:])

# Obtener el valor ASCII de un caracter
valorASCII = ord("A")
print(valorASCII)

# Metodo de strig que devuelve la ultima letra del abewcedario encontrada
cadena = "Hola x Como estas"
print(max(cadena))