# Conversor de decimal a binario
def conversor_decimal_binario(decimal):
    lista = []
    if decimal == "0":
        resultado = "0"
    else:
        decimal = int(decimal)
        while decimal != 1:
            digito = decimal % 2
            decimal = int(decimal/2)
            lista.append(digito)
        lista.append(1)
        lista_final = []
        for i in reversed(lista):
            lista_final.append(i)
    return ''.join(map(str,lista_final))

# Conversor de binario a decimal
def conversor_binario_decimal(binario):
    lista = []
    potencia=len(binario)
    for i in binario:
        potencia = potencia - 1
        digito = 2 ** potencia
        digito = digito * int(i)
        lista.append(int(digito))
        nuevo_numero = 0
        for j in lista:
            nuevo_numero = nuevo_numero + j
    return nuevo_numero

# Conversor de caracter binario
def conversor_caracter_binario(caracter):
    valor_bin = None
    lista_final = []
    for i in caracter:
        decimal = ord(i) 
        valor_bin = conversor_decimal_binario(decimal)
        lista_final.append(valor_bin.zfill(8))
    return ''.join(lista_final)

# Conversor de decimal a caracter 
def conversor_decimales_caracter(partes_decimales):
    lista_caracteres = []
    for decimal in partes_decimales:
        caracter = chr(decimal)
        lista_caracteres.append(caracter)
    return ''.join(lista_caracteres)  

# Conversor binario a decimal para caracter (lista)
def conversor_decimal_caracter_lista(lista):
    partes_decimales = []
    for k in lista:
        parte_dec = conversor_binario_decimal(k)
        partes_decimales.append(parte_dec)
    return partes_decimales

# Segmentar las cadenas binarias en 8 bits
def segmentador_binario(bin_caracter):
    partes = len(bin_caracter) // 8
    segmentos = []
    for i in range(partes):
        indice_bin = i * 8
        segmentos.append(bin_caracter[indice_bin : indice_bin + 8])
    return segmentos