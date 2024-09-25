import turtle
import time
import math

# Configuración de la ventana
ventana = turtle.Screen()
ventana.bgcolor("black")
ventana.title("Feliz 21 de Septiembre")

# Título principal
def escribir_titulo():
    titulo = turtle.Turtle()
    titulo.color("white")
    titulo.penup()
    titulo.hideturtle()
    titulo.goto(0, 220)  # Posición del título
    for size in range(28, 22, -1):
        titulo.clear()
        titulo.write("Feliz 21 de Septiembre", align="center", font=("Georgia", size, "bold"))
        time.sleep(0.1)

escribir_titulo()

# Función para dibujar una rosa con tallo y hojas
def dibujar_rosa_con_tallo(x, y, size):
    rosa = turtle.Turtle()
    rosa.speed(2)  # Velocidad de dibujo más lenta para un efecto más elegante
    rosa.hideturtle()
    turtle.colormode(255)
    
    # Pétalos de la rosa
    rosa.penup()
    rosa.goto(x, y)
    rosa.pendown()
    rosa.color("yellow")
    rosa.pensize(2)

    for i in range(36):  # 360 grados dividido en 36 pasos de 10 grados
        rosa.circle(size, 60)  # Tamaño de los pétalos
        rosa.left(120)
        rosa.circle(size, 60)
        rosa.left(60)
        rosa.left(10)  # Rotar un poco para el siguiente pétalo

    # Centro de la rosa
    rosa.penup()
    rosa.goto(x, y - size / 3)  # Mover el centro más arriba
    rosa.pendown()
    rosa.color("blue")
    rosa.begin_fill()
    rosa.circle(size / 5)
    rosa.end_fill()

    # Tallo más largo
    rosa.penup()
    rosa.goto(x, y - size - 100)  # Ajustar la posición del tallo
    rosa.pendown()
    rosa.color("green")
    rosa.width(4)
    rosa.left(90)
    rosa.forward(150)  # Longitud del tallo

# Dibujar la rosa
dibujar_rosa_con_tallo(15, 50, 50)

# Mensaje romántico
def escribir_mensaje():
    mensaje = turtle.Turtle()
    mensaje.color("white")
    mensaje.penup()
    mensaje.hideturtle()
    mensaje.goto(0, -250)  # Posición del mensaje
    for size in range(22, 18, -1):
        mensaje.clear()
        mensaje.write("Damaris.....♥ eres tan bonita como la primavera ♥", align="center", font=("Arial", size, "italic"))
        time.sleep(0.1)

escribir_mensaje()

ventana.mainloop()
