# Programa que determina el precio de la compra, el valor del descuento, el monto a pagar y el número de 
# unidades de obsequio de la compra de acuerdo a la cantidad de docenas.

# Solicitud de datos 
docenas=int(input("Ingrese los datos de los productos que adquirio\nDocenas: "))
precio=int(input("Precio: $"))
precio_inicial=precio*docenas

# Verificaciones
if docenas>3:
    monto_descuento=0.15*precio_inicial
    obsequio=docenas-3
else: 
    monto_descuento=0.10*precio_inicial
    obsequio=0
pago=precio_inicial-monto_descuento
obsequio_docenas=obsequio/1

# Resultados
print("El precio inicial por la(s) ", docenas, "docena(s) era de: $", precio_inicial)
print("El valor del descuento es de: $", monto_descuento)
print("La cantidad a pagar es de: $", pago)
print("Debido a que compró ", docenas, " docenas, se le obsequiarán ",obsequio, " unidades o ", round(obsequio_docenas,2), " docenas")

# Créditos
print("====================================")
print("Programa hecho por Alejandro Giraldo")
print("====================================")

