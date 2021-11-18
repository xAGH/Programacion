# Realice el siguiente programa e indique que hace.

# Declaracíon de variables
EdadJuan=int(input("Indique la edad de Juan: "))
EdadMario=int(input("Indique la edad de Mario: "))
EdadPedro=int(input("Indique la edad de Pedro: "))

# Determinar quiénes son contemporáneos

# Los 3
if EdadJuan == EdadMario and EdadMario==EdadPedro:
    contemporaneos="Juan, Pedro y Mario son contemporáneos"

# Solo 2
elif EdadJuan==EdadMario:
    contemporaneos="\nSolo Juan y Mario son contemporáneos\n"
elif EdadJuan==EdadPedro:
    contemporaneos="\nSolo Juan y Pedro son contemporáneos\n"
elif EdadPedro==EdadMario:
    contemporaneos="\nSolo Pedro y Mario son contemporáneos\n"

# Ninguno
else: 
    contemporaneos="\nNinguno de los tres son contemporáneos\n"

# Resultado:
print(contemporaneos)

# Créditos
print("====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================\n")
