# Programa que solicita 10 valores y da a conocer distintos datos

negativos=0
positivos=0
multiplos15=0
pares=0
print("Ingrese 10 números")
for i in range(1, 11):
    numero=(int(input(f"Numero #{i}:")))
    if numero>=0:
        positivos+=1
    else:
        negativos+=1
    if numero%15==0:
        multiplos15+=1
    if numero%2==0:
        pares+=1

print(f"\nLa cantidad de:\nNúmeros negativos={negativos}")
print(f"Números positivos={positivos}")
print(f"Múltiplos de 15={multiplos15}")
print(f"Números pares={pares}")

# Créditos
print("\n====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================\n")
