# Programa que determina el deswcuento según el artículo ingresado

# Solicitud e impresión de datos
carro=input("Ingrese el carro que está a la venta:\n1. Ford Fiesta.\n2. Ford Focus\n3. Otro\nArtículo: ")
if carro=="1" or carro.title()=="Ford Fiesta":
    descuento="cuenta con un descuento del 5%."
elif carro=="2" or carro.title()=="Ford Focus":
    descuento="cuenta con un descuento del 10%"
elif carro=="3" or carro.title()=="Otro":
    otro=input("Ingrese el artículo: ")
    descuento="no está a la venta o no cuenta con descuento"
else:
    print("Ingresó un valor fuera de los parámetros")
    descuento="no es válido"
print("El artículo que ha seleccionado", descuento)

# Créditos
print("\n====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================\n")
