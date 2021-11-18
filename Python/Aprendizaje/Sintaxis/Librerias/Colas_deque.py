# Deque es un módulo de la librería collections que trabaja con listas, permitiendo en estas nuevas funciones.
from collections import deque

# Se define una lista de acuerdo con el módulo deques:

lista = deque([1, 2, 3, 4, 5, 6])

# Deque permite borrar elementos en oden de pila, es decir, el último objeto igual que python por defecto.
lista.pop() # Elimina el último valor, en este caso el 6. La lista quedaría como deque([1, 2, 3, 4, 5])

# Pero tambien permite eliminar objetos de las listas en orden de cola, es decir, eliminar el primer elemento ingresado en esta.
lista.popleft() # Elimina el primer valor, en este caso el 1. La lista quedaría La lista quedaría como deque([2, 3, 4, 5])