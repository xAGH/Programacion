"""Programa que de acuerdo a 3 notas entregadas de un alumno, calcula su promedio
y segun el resultado arroja ciertas noticias"""
nombre=input("Ingrese el nombre del alumno: ")
n1=int(input("Ingrese la nota #1 de ", nombre))
n2=int(input("Ingrese la nota #2 de ", nombre))
n3=int(input("Ingrese la nota #3 de ", nombre))
promedio=(n1+n2+n3)/3
promedio=round(promedio,2)
if (promedio>=7):
    print(nombre, " pasa")
else: 
    print(nombre, " repite")
print("===================================")
print("Hecho por Alejandro Giraldo Herrera")
