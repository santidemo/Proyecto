import random
import turtle
import time

luego = 0.06

# Configuración inicial del juego
vi = turtle.Screen()
vi.title("Gusanito")
vi.bgcolor("green")
vi.setup(width=600, height=600)
vi.tracer(0)

# Configuración de la cabeza
cabeza = turtle.Turtle()
cabeza.speed(10)
cabeza.shape("square")
cabeza.goto(0, 0)
cabeza.direction = "stop"
cabeza.color("red")
cabeza.penup()

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.penup()
comida.goto(0, 100)
comida.color("white")

# Función de movimiento
def mov():
    if cabeza.direction == "Arriba":
        y = cabeza.ycor()
        cabeza.sety(y + 10)
    if cabeza.direction == "Abajo":
        y = cabeza.ycor()
        cabeza.sety(y - 10)
    if cabeza.direction == "Izquierda":
        x = cabeza.xcor()
        cabeza.setx(x - 10)
    if cabeza.direction == "Derecha":
        x = cabeza.xcor()
        cabeza.setx(x + 10)

# Introducir teclado
def Arriba():
    cabeza.direction = "Arriba"
def Abajo():
    cabeza.direction = "Abajo"
def Izquierda():
    cabeza.direction = "Izquierda"
def Derecha():
    cabeza.direction = "Derecha"

vi.listen()
vi.onkeyrelease(Arriba, "Up")
vi.onkeyrelease(Abajo, "Down")
vi.onkeyrelease(Derecha, "Right")
vi.onkeyrelease(Izquierda, "Left")
