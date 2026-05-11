from turtle import *
from random import randint

t = Turtle()

t.speed(0)

def main():
    star_frac(t, 100)

def sq_frac(t, size, step = 50):
    if size == 0 or step == 0:
        return
    t.pu()
    t.fd(size / 1.5)
    t.lt(10)
    sq(t, size)
    sq_frac(t, size - 1, step - 1)


def sq(t, size):
    t.pd()
    for _ in range(4):
        t.fd(size)
        t.rt(90)

def star_frac(t, size):
    if size < 10:
        return
    for _ in range(5):
        t.fd(size)
        star_frac(t, size / 3)
        t.lt(216)

# def random_color():
#     return (randint(0, 255), randint(0, 255), randint(0, 255))

main()
mainloop()
