# Programa para guardar contacto de personas con nombre y telefono, listarlos y modificarlos

# Importar módulos para trabajar con el sistema operativo
import os

#------------------------------------------------------------------
def cargarContactos(contactos):
    os.system("cls")
    continuar="si"
    while continuar in "s,S,SI,SÍ,Si,Sí,si,sI,sÍ":
        nombre=input("Ingrese el nombre del contacto a crear: ")
        nombre=nombre.title()
        telefono=input("Ingrese número de teléfono: ")
        contactos.append([nombre,telefono])
        continuar=input("Ingresar otro contacto [si/no]: ")
    return(contactos)
#------------------------------------------------------------------
def listarContactos(contactos):
    os.system("cls")
    contactos.sort()
    print("Listado de los contactos disponibles")
    print("Nro.\tNombre\tTeléfono")
    i=1
    for nombre in contactos:
        print(f"{i}\t{nombre[0]}\t{nombre[1]}")
        i+=1
#------------------------------------------------------------------
def editarContactos(contactos):
    os.system("cls")
    caso=0
    while caso<=0 or caso>2:
        caso=int(input("¿Qué desea moodificar?\n1. Nombre.\n2. Teléfono\nOpción: "))
    if caso==1:
        nombreBuscar=input("Escriba el nombre del contacto a modificar: ").title()
        j=0
        for i in contactos:
            if i[0]==nombreBuscar:
                nombre=input("Ingrese el nuevo nombre: ")
                i[0]=nombre
                j=1
        if j==0:
            print(f"No existe contacto con el nombre {nombreBuscar}")
    elif caso==2:
        nombreBuscar=input("Escriba el nombre del contacto a modificar: ").title()
        j=0
        for i in contactos:
            if i[0]==nombreBuscar:
                telefono=input("Ingrese el nuevo número teléfonico: ")
                i[1]=telefono
                j=1
        if j==0:
            print(f"No existe contacto con el nombre {nombreBuscar}")
#------------------------------------------------------------------
def menu(contactos):
    opcion=0
    while opcion<=0 or opcion>4:
        print("_"*30)
        print("Programa para administrar una agenda")
        print("_"*30)
        print("1. Agregar Contactos.\n2. Modificar Contactos.\n3. Listar Contactos.\n4. Salir.")
        print("_"*30)
        opcion=int(input("Ingrese opción: "))
    if opcion==1:
        cargarContactos(contactos)
    elif opcion==2:
        editarContactos(contactos)
    elif opcion==3:
        listarContactos(contactos)
    else:
        print("Hasta luego.")
        exit()
#------------------BLOQUE PRINCIPAL------------------
contactos = cargarContactos([])

while True:
    menu(contactos)



