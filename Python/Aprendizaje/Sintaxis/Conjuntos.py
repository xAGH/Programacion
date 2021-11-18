# Los conjuntos o sets son colecciones no ordenadas de objetos únicos. Python provee
# este tipo de datos "por defecto" al igual que otras colecciones más convencionales 
# como las listas, tuplas y diccionarios. Estas colecciones, detectará si hay
# elementos repetidos y al imprimirlos solo mostrará uno de ellos.

# Para definir un conjunto, se encierran los objetos entre llaves separados por comas
# o se puede usar la funcion set: conjunto = set(<objetos separados por comas>)
conjunto = {2, 3, 4, 5, 6, "Hola", "Mundo"} # o conjunto = set(2, 3, 4, 5, 6, "Hola", "Mundo")

# Los conjuntos añaden elementos de acuerdo a su valor, por ejemplo, ubicando los números
# de menor a mayor de acuerdo a los elementos ya existentes en el conjunto.

# Se añade un valor menor a los del conjunto:
conjunto.add(1)
# Ahora el conjunto es conjunto = {1, 2, 3, 4, 5, 6, "Hola", "Mundo"} Añadiendo el
# 1 al principio del mismo.

# Se añade un valor mayor a los del conjunto.
conjunto.add(7)
# Ahora el conjunto es conjunto = {1, 2, 3, 4, 5, 6, 7 "Hola", "Mundo"} Añadiendo el
# 7 al final de los números.

# Se pueden verficar elementos de un conjunto con in:
2 in conjunto # Devuelve True

# Como curiosidad, si le pasamos como parametro a un set una cadena, esta se almacenará 
# desorganizadamente y no en el orden estipulado, además de almacenar un único objeto por valor,
# es decir, elimina los objetos repetidos. Ejemplo:
cadena = "Holaaa mundo"
conjunto_cadena = set(cadena) # Se almacena --> {'d', 'o', 'n', 'l', ' ', 'a', 'm', 'u', 'H'} en este caso, pero cada caso es diferente