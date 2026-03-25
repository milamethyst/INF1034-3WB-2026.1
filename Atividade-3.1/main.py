from turtle import *
from random import randint

t = Turtle()
t.speed(0)

def main():
    x_max = 300
    y_max = 300
    x_min = 150
    y_min = 100

    plano_cartesiano(700, 'black')

    x = randint(x_min, x_max)
    y = randint(y_min, y_max)
    lados = int(textinput('Número de lados', 'Insira o número de lados para o polígono (mínimo 3)'))
    cor = textinput('Cor do polígono', 'Insira a cor desejada para o polígono')
    poligono(x, y-80, 500/lados, lados, cor)

    x = randint(x_min, x_max)
    y = randint(y_min, y_max)
    lados = int(textinput('Número de lados', 'Insira o número de lados para o polígono (mínimo 3)'))
    cor = textinput('Cor do polígono', 'Insira a cor desejada para o polígono')
    poligono(-x-100, y-80, 500/lados, lados, cor)

    x = randint(x_min, x_max)
    y = randint(y_min, y_max)
    cor = textinput('Cor da cruz', 'Insira a cor desejada para a cruz')
    cruz(x, -y, 50, cor)

    x = randint(x_min, x_max)
    y = randint(y_min, y_max)
    cor = textinput('Cor da estrela', 'Insira a cor desejada para a estrela')
    estrela(-x-100, -y, 50, cor)
    
    cor = textinput("Obter cor", "Digite uma cor para a espiral")
    espiral(x+50, -y-100, 75, cor)


def cruz(x, y, size, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.fd(size)
        t.rt(90)
        t.fd(size)
        t.lt(90)
        t.fd(size)
        t.rt(90)
        t.fd(size)
        t.rt(90)
        t.fd(size)
        t.lt(90)
        t.fd(size)
        t.rt(90)
    t.end_fill()

def estrela(x, y, size, color):
    t.pu()
    t.goto(x, y)
    t.color(color)
    t.begin_fill()
    for i in range(5):
        t.fd(size)
        t.lt(72)
        t.fd(size)
        t.rt(144)
    t.end_fill()

def poligono(x, y, size, sides, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color(color)
    t.begin_fill()
    for _ in range(sides):
        t.fd(size)
        t.lt(360/sides)
    t.end_fill()
    t.setheading(0)

def espiral(x, y, size, color):
    t.pu()
    t.goto(-(2.5*x), y)
    t.pd()
    t.color(color)
    for i in range(size):
        t.fd(i * 1.25)
        t.lt(30)

def plano_cartesiano(size, color):
    t.pu()
    t.goto(0, -size/2)
    t.pd()
    t.color(color)
    t.lt(90)
    t.fd(size)
    t.stamp()
    t.pu()
    t.goto(-size, 0)
    t.pd()
    t.rt(90)
    t.fd(size*2)
    t.stamp()

main()
mainloop()