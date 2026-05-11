from turtle import *
from random import randint

t = Turtle()

t.speed(0)

def main():
    t.lt(90)
    # tree_frac(t, 150, 30, 1)

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

# def tree_frac(t, size, angle, level):
    # if size < 40:
    #     return

    # t.fd(size)
    # t.rt(angle)
    # t.fd(size)
    # tree_frac(t, size * 0.08, angle, level - 1)
    # t.back(size)

    # t.lt(angle * 2)
    # t.fd(size)
    # tree_frac(t, size * 0.08, angle, level - 1)
    # t.back(size)

    # t.rt(angle)
    # t.back(size)

# def random_color():
#     return (randint(0, 255), randint(0, 255), randint(0, 255))

main()
mainloop()
