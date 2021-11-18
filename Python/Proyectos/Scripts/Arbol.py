veces=int(input("Ingrese la 'cantidad de pisos' que tendrá el árbol: "))
a = "*"
b = " "
j = 0

for i in range(veces):
    if i == 0:
        b = b * veces
        print(b, a)
        a = a + "**"
        repeti = veces - 1
        b = " " * repeti
    else:
        print(b,a,b)
        a = a + "**"
        repeti -= 1
        b = " " * repeti
for j in range(int(veces / 3)):
    c = "*" * int(i / 3)
    b = " " * (veces - 1)
    print(b, c)