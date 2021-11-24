# Las variables se pueden asignar con < - o con =
x = 1
y <- 3

# Declarar vectores
vector <- c(1:10) # Es lo mismo que declarar c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

nuevo_vector <- c(1, 1, 1, 2, 3, 4, 5, 9, 8)

# Declara Factores: Los factores son como un filto que devuelve los niveles o
# las llaves que se presentan en su contenido 1 vez, es decir, aunque hayan elementos
# con el mismo valor, en el factor solo se observara una vez dicho valor.
Factor <- factor(nuevo_vector) # Devuelve -> 1,2,3,4,5,8,9 ; Levels: 1, 2, 3, 4, 5

nuevo_vector < 6 # -> La condición itera sobre cada elemento y devuelve true o false
# según el caso. En este caso devuelve -> FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, TRUE, TRUE

# Los vectores de igual tipo y tamaño se pueden operar, dando como resultado lo obtenido de la operación
# por cada elemento de igual indice de los dos vectores, por ejemplo:
suma_vectores <- c(1,2,3) + c(4,5,6) # Devuelve -> c(5, 7, 9)


year <- c(1985, 1999, 2010, 2002)
# Esto le asigna un nombre a cada año respectivo a su indice.
names(year) <- c("Pelicula 1", "Pelicula 2", "Pelicula 3", "Pelicula 4")
# sort acomoda los elementos de menor a mayor
year_sorted <- sort(year) # Devuelve -> Pelicula 1: 1985, Pelicula 2: 1999, Pelicula 4: 2002, Pelicula 3: 2010

# max() y min() hallan los valores máximos y mínimos dentro de un vector
max(year) # Devuelve -> 2010
min(year) # Devuelve -> 1985

# mean() sirve para sacar el promedio de los numeros de un vector.
mean(c(1,2,3)) # Devuelve -> 2

# summary() devuelve datos como la media, la mediana, mínimo, etc
summary(c(1,2,3)) # Devuelve -> Min: 1.0 ; 1st Qu.: 1.5 ; Median: 2.0 ; Mean: 2.0 ; 3rd Qu.: 2.5 ; Max: 3.0