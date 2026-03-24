from turtle import *
from time import sleep

t = Turtle()

t.speed(0)

def main():
    # Bandeiras fáceis
    # Holanda/Países Baixos
    retangulo(-450, 300, 900, 200, '#ae1c28')
    retangulo(-450, 100, 900, 200, '#ffffff')
    retangulo(-450, -100, 900, 200, '#21468b')
    base()

    # Itália
    retangulo(-450, 300, 300, 600, '#009246')
    retangulo(-150, 300, 300, 600, '#ffffff')
    retangulo(150, 300, 300, 600, '#ce2b37')
    base()

    # Bandeiras médias
    # Gana
    retangulo(-450, 300, 900, 200, '#ce1126')
    retangulo(-450, 100, 900, 200, '#fcd116')
    retangulo(-450, -100, 900, 200, '#006b3f')
    estrela(-100, 25, 75, 'black')
    base()

    # Cuba
    for i in range(5):
        if (i % 2 == 0):
            color = '#002a8f'
        else:
            color = '#ffffff'
        retangulo(-450, 300-(i*120), 900, 120, color)
    triangulo(-450, 300, 600, '#cb1515')
    estrela(-350, 25, 75, '#ffffff')
    base()
    
    # Palestina
    retangulo(-450, 300, 900, 200, '#000000')
    retangulo(-450, 100, 900, 200, '#ffffff')
    retangulo(-450, -100, 900, 200, '#007a3d')
    t.pu()
    t.goto(-450, 300)
    t.pd()
    t.color('#ce1126')
    t.begin_fill()
    t.rt(45)
    t.fd(425)
    t.rt(90)
    t.fd(425)
    t.rt(135)
    t.fd(600)
    t.end_fill()
    t.setheading(0)
    base()

    # Bandeiras difíceis
    # República Centro-Africana
    retangulo(-450, 300, 900, 150, '#003082')
    retangulo(-450, 150, 900, 150, '#ffffff')
    retangulo(-450, 0, 900, 150, '#289728')
    retangulo(-450, -150, 900, 150, '#ffce00')
    retangulo(-75, 300, 150, 600, '#d21034')
    estrela(-350, 240, 50, '#ffce00')
    base()

    # África do Sul
    retangulo(-450, 300, 900, 200, '#e03c31')
    retangulo(-450, 100, 900, 200, '#ffffff')
    retangulo(-450, -100, 900, 200, '#001489')
    retangulo(-450, 300, 112.5, 600, '#ffffff')
    triangulo(-337.5, 300, 600, '#ffffff')
    retangulo(-450, 60, 900, 120, '#007749')
    retangulo(-450, 300, 50, 600, '#007749')
    triangulo(-400, 300, 600, '#007749')
    triangulo(-450, 235, 470, '#ffb81c')
    triangulo(-450, 202.5, 405, '#000000')
    base()

    # Geórgia
    t.pu()
    t.goto(-65, 300)
    t.pd()
    t.color('#ff0000')
    t.begin_fill()
    for _ in range(2):
        t.fd(130)
        t.rt(90)
        t.fd(235)
        t.lt(90)
        t.fd(385)
        t.rt(90)
        t.fd(130)
        t.rt(90)
        t.fd(385)
        t.lt(90)
        t.fd(235)
        t.rt(90)
    t.end_fill()
    cruz(-278, 244, 41)
    cruz(237, 244, 41)
    cruz(-278, -121, 41)
    cruz(237, -121, 41)
    base()

    # Grécia
    for i in range(8):
        if (i % 2 == 0):
            color = '#0d5eaf'
        else:
            color = '#ffffff'
        retangulo(-450, 300-(i*66), 900, 66, color)
    color = '#0d5eaf'
    retangulo(-450, -228, 900, 72, color)
    retangulo(-450, 300, 320, 320, color)
    t.color('#ffffff')
    t.pu()
    t.goto(-323, 300)
    t.pd()
    t.begin_fill()
    for _ in range(2):
        t.fd(66)
        t.rt(90)
        t.fd(132)
        t.lt(90)
        t.fd(127)
        t.rt(90)
        t.fd(66)
        t.rt(90)
        t.fd(127)
        t.lt(90)
        t.fd(132)
        t.rt(90)
    t.end_fill()
    base()


def retangulo(x, y, fd_x, fd_y, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.fd(fd_x)
        t.rt(90)
        t.fd(fd_y)
        t.rt(90)
    t.end_fill()

def cruz(x, y, fd):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    for _ in range(2):
        t.fd(fd)
        t.rt(90)
        t.fd(fd)
        t.lt(90)
        t.fd(fd)
        t.rt(90)
        t.fd(fd)
        t.rt(90)
        t.fd(fd)
        t.lt(90)
        t.fd(fd)
        t.rt(90)
    t.end_fill()

def estrela(x, y, size, color):
    t.pu()
    t.goto(x, y)
    t.color(color)
    t.begin_fill()
    for i in range(5):
        t.fd(size)
        t.left(72)
        t.forward(size)
        t.right(144)
    t.end_fill()

def triangulo(x, y, size, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color(color)
    t.begin_fill()
    t.rt(30)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.end_fill()
    t.setheading(0)
    
def base():
    t.pu()
    t.color('black')
    t.goto(-450, 300)
    t.pd()
    for _ in range(2):
        t.fd(900)
        t.rt(90)
        t.fd(600)
        t.rt(90)
    
    sleep(5)
    t.clear()


main()
mainloop()