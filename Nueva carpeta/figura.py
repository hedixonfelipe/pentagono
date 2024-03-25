import turtle
import random

def dibujar_poligono(tortuga, lados, color):
    angulo = 360 / lados
    tortuga.color(color,"black")
    

    for _ in range(lados):
        tortuga.forward(100)
        tortuga.left(angulo)

def dibujar_figuras_desde_triangulo_a_octagono():
    ventana = turtle.Screen() 
    ventana.bgcolor("white")
    ventana.title("Dibujando polígonos")

    tortuga = turtle.Turtle()
    tortuga.shape("turtle")
    tortuga.speed(2)

    colores = ["orange","cyan","yellow","magenta", "red","blue","green","purple"]

    for lados in range(3, 9):
        tortuga.penup()
        tortuga.setposition(0, 0)
        tortuga.pendown()
        color = random.choice(colores)  
        dibujar_poligono(tortuga, lados, color)

    ventana.mainloop()

dibujar_figuras_desde_triangulo_a_octagono()
