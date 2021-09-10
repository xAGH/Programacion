# Escribe un programa que pueda calcular el factorial de varios números dados. Los resultados deben de ser impresos en una secuencia separadas por comas en una sola linea.

def factorial(numero):
    if numero == 0:
        print('0') 
    factorial = 1
    for i in range(1, numero+1): 
        factorial = factorial * i
    return factorial

i=0







