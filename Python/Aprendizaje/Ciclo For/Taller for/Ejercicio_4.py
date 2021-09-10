# Programa que realiza la serie de Fibonacci de n numeros que se solicitan

veces=int(input("Ingrese el número de veces que se repetirá la secuencia: "))
f0=0
f1=1
fn=0
for i in range(veces):
    print(fn, end=", ")
    f0=f1
    f1=fn
    fn=f0+f1

# Créditos
print("\n====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================\n")
