import turtle
import time
import random

posponer=0.1

# Marcador
score = 0
high_score = 0


# Configuracion de la ventana
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("Green")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("orange")
comida.penup()
comida.goto(0,100)

segmentos = []

# Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Score: 0\tHigh Score: 0",align = "center", font = ("Courier", 24, "normal"))

# Funciones
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izq():
    cabeza.direction = "left"
def der():
    cabeza.direction = "right"

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)
        
# Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izq, "Left")
wn.onkeypress(der, "Right")

while True:
    wn.update()

    # Colision con los bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        # Esconder segmentos
        for segmento in segmentos:
            segmento.goto(2000, 2000)

        # Limpiar lista de segmentos
        segmentos.clear()

        # Resetear marcador
        score = 0
        texto.clear()
        texto.write("Score: {}\tHigh Score: {}".format(score, high_score),
                align = "center", font = ("Courier", 24, "normal"))

    # Colision con la comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        nuevo_segemento = turtle.Turtle()
        nuevo_segemento.speed(0)
        nuevo_segemento.shape("square")
        nuevo_segemento.color("grey")
        nuevo_segemento.penup()
        segmentos.append(nuevo_segemento)
        
        #Aumentar marcador
        score+=10

        if score > high_score:
            high_score = score

        texto.clear()
        texto.write("Score: {}\tHigh Score: {}".format(score, high_score),
                align = "center", font = ("Courier", 24, "normal"))

    # Animacion de movimiento de la serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x, y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

        
    mov()

    #Colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = "stop"

            # Esconder los segmentos
            for segmento in segmentos:
                segmento.goto(2000, 2000)
            
            # Limpiar la lista de los segmentos
            segmentos.clear()

            # Resetear marcador
            # Resetear marcador
            score = 0
            texto.clear()
            texto.write("Score: {}\tHigh Score: {}".format(score, high_score),
                    align = "center", font = ("Courier", 24, "normal"))

    time.sleep(posponer)