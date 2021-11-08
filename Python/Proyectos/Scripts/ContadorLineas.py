# Ruta absoluta F:\SENA\Hugo Hernan Henao\Trimestre IV\Evidencias\QuickSort\Script\src\App.java
# Ruta relativa ./App.java

ruta = "RUTA ABSOLUTA O REALTIVA DEL ARCHIVO" 

try:
    with open(ruta, "rb") as file:
        contador = 0
        for linea in file:
            if not linea.isspace():
                contador += 1

        print(contador)

except:
    print("Archivo no encontrado")
