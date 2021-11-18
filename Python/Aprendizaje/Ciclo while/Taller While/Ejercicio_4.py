# Programa que verifica si una letra está en una frase indicada.

# Declaración de variables
palabra=input("\nIngrese una palabra o frase: ")
letra=input("Ingrese una letra: ")
i=0
siEsta=0

# Validación
if len(letra)>1:
    print("Debe ser solo una letra")
else:
    # Resultado
    print("La letra '",letra, "' se encuentra en la posición",sep="",end=": ")
    while i<len(palabra):
        if palabra[i]==letra:
            siEsta+=1
            print(i+1,end=", ") # Pongo i+1 ya que este programa seria confuso para aquellos que no sepan que las matrices empiezan desde 0, por lo tanto entenderían mejor el programa*
        i+=1
    if siEsta==0:
        print("Ninguna letra en la palabra o frase coincide con la letra",letra)
    else:
        print("\nLa letra",letra,"se encontró",siEsta,"veces")
    
# Créditos
print("\n====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================\n")

    