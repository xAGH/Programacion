# Una lista sirve para guardar objetos, al igual que un vector, sin embargo, estas
# permiten almacenar diferentes tipos de datos.

movies <- list("Toy Story", 1995, c("Animation", "Adventure", "Comedy"))

movies

# Para acceder a los objetos en una lista se indica su posicion entre corchetes
movies[3]

# En las listas tambien se pueden usar identificadores para cada valor, ejemplo:

movies_keys <- list(name="Toy Story", 
                    year=1995, 
                    genre= c("Animation", "Adventure", "Comedy"))
# De esta forma es mas legible el codigo a la hora de ser ejecutado
movies_keys

# Para acceder al valor de una llave de una lista, se utiliza el signo $ o 
# se indica el nombre de la llave entre comillas y corchetes. Asi:
movies_keys$name

movies_keys["name"]

#Para añadir un valor a esta lista, se utiliza el operador de declaracion con la
# llave y valor del nuevo registro:
movies_keys["age"] <- 5


# *NOTA: Las listas pueden tener o no llave identificadora, lo que permite
# hacer cosas como esta: list(vector=c(1,2), 3, 4, 5, "Asi)*

# Para reemplazar el valor de una llave, se utiliza el operador de declaracion 
# mas el nombre de la llave y el nuevo valor, ejemplo:
movies_keys["age"] <- 4

movies_keys

# Para ocultar llaves y su valor, se sobre escribe la llave con el operador de 
# declaracion y con el valor de NULL, asi:
movies["age"] <- 5
