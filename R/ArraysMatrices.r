vector <- c("Posicion1", "Posicion2", "Posicion3", "Posicion4", "Posicion5") # Se
# inicializa un vector

nuevo_array <- array(vector, c(2, 3)) # Se inicializa un array, pasándole el vector
# y otro vector el cual serán las dimensiones del array, es decir, columnas y filas
# respectivamente

nuevo_array # Esto nos devuelve un una tabla con los valores dados, en caso de hacer mas celdas
# que datos, estos se repetiran desde el incio hasta satisfacer a las celdas.

nuevo_array

# Para acceder a un elemento de un array se especifica su numero de fila y de columna
# Entre corchetes:

nuevo_array[1:2,2:3] # Se puede especificar tambien un intervalo de filas o de columnas.

# Las matrices tienen la misma funcionalidad que los arrays, sin embargo,e stas son mas 
# flexibles a la hora de maquetar el trabajo

matriz <- matrix(vector, nrow = 2, ncol = 3, byrow = TRUE) # Sintaxis para crear una matriz
# El argumento byrow permite organizar e imprimir los valores con orden de fila, es decir,
# de izquierda a derecha en vez de arriba hacia abajo como hacen los arrays o las
# matrices de forma predeterminada.

matriz

# Para acceder a los elentos de una matriz, se utiliza la misma sintaxis que con los
# arrays

matriz[1,2]

