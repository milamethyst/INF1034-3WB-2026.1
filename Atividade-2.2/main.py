from turtle import *
from time import sleep

t = Turtle()

t.speed(0)

def main():
    # Bandeiras fáceis
    # Holanda/Países Baixos
    facil(-450, 300, 900, 200, '#ae1c28')
    facil(-450, 100, 900, 200, '#ffffff')
    facil(-450, -100, 900, 200, '#21468b')
    base()

    # Itália
    facil(-450, 300, 300, 600, '#009246')
    facil(-150, 300, 300, 600, '#ffffff')
    facil(150, 300, 300, 600, '#ce2b37')
    base()

    # Bandeiras médias
    # Gana (FAZER ESTRELA!!!!)
    facil(-450, 300, 900, 200, '#ce1126')
    facil(-450, 100, 900, 200, '#fcd116')
    facil(-450, -100, 900, 200, '#006b3f')
    """
    t.pu()
    t.goto(0, 100)
    t.color('black')
    t.begin_fill()
    for side in range(5):
        t.fd(200)
        t.rt(120)
        t.fd(200)
        t.rt(72 - 120)
    t.end_fill()
    base()
    """

    # Bandeiras difíceis
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

    cruz(-278, 244)
    cruz(237, 244)
    cruz(-278, -121)
    cruz(237, -121)

    base()


def facil(x, y, fd_x, fd_y, color):
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

def cruz(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    for _ in range(2):
        t.fd(41)
        t.rt(90)
        t.fd(41)
        t.lt(90)
        t.fd(41)
        t.rt(90)
        t.fd(41)
        t.rt(90)
        t.fd(41)
        t.lt(90)
        t.fd(41)
        t.rt(90)
    t.end_fill()

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