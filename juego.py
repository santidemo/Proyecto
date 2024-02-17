from confi2 import *

# Cuerpo de la serpiente
crece = []

while True:
    vi.update()

    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"
        for i in crece:
            i.goto(1000, 1000)
        crece.clear()

    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        come_crece = turtle.Turtle()
        come_crece.speed(10)
        come_crece.shape("square")
        come_crece.color("dark red")
        come_crece.penup()
        crece.append(come_crece)

    cantidad = len(crece)
    for i in range(cantidad - 1, 0, -1):
        x = crece[i - 1].xcor()
        y = crece[i - 1].ycor()
        crece[i].goto(x, y)

    if cantidad > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        crece[0].goto(x, y)

    mov()

    for i in crece:
        if cabeza.xcor() == i.xcor() and cabeza.ycor() == i.ycor():
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = "stop"
            for segmento in crece:
                segmento.goto(1000, 1000)
            crece.clear()

    time.sleep(luego)
