# Traductor que convierte decimales y caracteres a binario y visceversa. 

# Importación de la libreria de conversores
from conversor_binario import *

# Solicitud de datos decimal a binario
def solicitud_decimal_binario():
    bandera = True

    while bandera:
        decimal = input("\nIngrese el número decimal (X para salir): ")
        
        if decimal.upper() == "X":
            print("___________\nSaliendo...\n\n")
            bandera = False
        else: 
            print(conversor_decimal_binario(decimal))

# Solicitud de datos binario decimal
def solicitud_binario_decimal():
    bandera = True 

    while bandera: 
        error = 0
        binario = input("\nIngrese el número binario (X para salir): ")
        for a in binario:
            if a >= "2" and a <= "9":
                error = 1
        if error == 1:
            print("Solo se permiten '0' y '1'")
            error = 0
        elif binario.upper() == "X":
            print("___________\nSaliendo...\n\n")
            bandera = False
        else: 
            print(conversor_binario_decimal(binario))

# Solicitud de caracteres binario
def solicitud_caracter_binario():
    bandera = True 

    while bandera: 
        caracter = input("\nIngrese el/los caracter(es) (salir123 para salir): ")
        if caracter == "salir123":
            print("___________\nSaliendo...\n\n")   
            bandera = False
        else:
            print(conversor_caracter_binario(caracter))

# Solicitud de binario caracteres 
def solicitud_binario_caracter():
    bandera = True 

    while bandera: 
        error = 0
        bin_caracter = input("\nIngrese la cadena binaria: (X para salir): ")
        bin_caracter = bin_caracter.replace(" ", "")
        
        for j in bin_caracter:
            if j >= "2" and j <= "9":
                error = 1
        if error == 1:
            print("Solo se permiten '0' y '1'")
            error = 0
        elif bin_caracter.upper() == "X":
            print("___________\nSaliendo...\n\n")
            bandera = False
        else:
            segmentos = segmentador_binario(bin_caracter.zfill(8))
            partes_decimales = conversor_decimal_caracter_lista(segmentos)
            caracteres = conversor_decimales_caracter(partes_decimales)
            print(f"\n{caracteres}\n")

# "Menú principal"
def main():
    bandera = True
    while bandera:
        print("__________________________________________________________________")
        entrada = input("Seleccione el número correspondiente de la conversión a realizar:\n1. De decimal a binario.\n2. De binario a decimal.\n3. De caracter a binario.\n4. De binario a caracter.\n5. Salir.\nOpción: ")
        print("__________________________________________________________________")

        if entrada == "1":
            solicitud_decimal_binario()
        elif entrada == "2":
            solicitud_binario_decimal()
        elif entrada == "3":
            solicitud_caracter_binario()
        elif entrada == "4":
            solicitud_binario_caracter()
        elif entrada == "5":
            bandera = False
        else:
            print("\nIngrese una opción correcta.\n")

if __name__ == "__main__":
    main()
# Llamada de la función principal

