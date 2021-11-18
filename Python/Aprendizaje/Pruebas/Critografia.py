#Critografia E=3, A=4, O=0, B=8
#Sapo=54p0 ; ALEJO= 413J0
palabra=input("Ingrese una palabra o frase: ").upper()
i=0
nueva=""
while(i<len(palabra)):
    if(palabra[i]=="a"):
        nueva=nueva+"4"
    elif (palabra[i]=="e"):
        nueva=nueva+"3"
    elif (palabra[i]=="l"):
        nueva=nueva+"1"
    elif (palabra[i]=="s"):
        nueva=nueva+"5"
    elif (palabra[i]=="o"):
        nueva=nueva+"0"
    elif (palabra[i]=="t"):
        nueva=nueva+"7"
    elif (palabra[i]=="g"):
        nueva=nueva+"6"
    elif (palabra[i]=="b"):
        nueva=nueva+"8"
    else:
        nueva=nueva+palabra[i]
    i+=1
print(nueva)