from turtle import *
from random import randint
from time import sleep

t = Turtle()

t.speed(0)
colormode(255)
t.screen.bgcolor('black')

def main():
    t.teleport(-175, 50)
    star_frac(t, 300)

    sleep(5)
    t.clear()
    t.setheading(90)
    t.teleport(250, -100)
    sq_frac(t, 80)

    sleep(5)
    t.clear()
    t.setheading(90)
    t.teleport(0, -300)
    t.color(tree_levels[0])
    tree_frac(t, 100, 30)
    
    sleep(5)
    t.clear()
    t.setheading(0)
    t.teleport(-250, -200)
    triangle_frac(t, 500)

def random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def sq_frac(t, size, step = 100):
    if size == 0 or step == 0:
        return
    t.pu()
    t.fd(size / 1.5)
    t.lt(10)
    t.begin_fill()
    t.color(random_color())
    sq(t, size)
    t.end_fill()
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
        t.color(random_color())
        t.fd(size)
        star_frac(t, size / 3)
        t.lt(216)

def tree_frac(t, size, angle, level = 0):
    if size < 40:
        return
    if len(tree_levels) <= level:
        tree_levels.append(random_color())

    t.color(tree_levels[level])

    t.fd(size)
    t.rt(angle)
    t.fd(size)
    tree_frac(t, size * 0.8, angle, level + 1)
    t.color(tree_levels[level])
    t.back(size)

    t.lt(angle * 2)
    t.fd(size)
    tree_frac(t, size * 0.8, angle, level + 1)
    t.color(tree_levels[level])
    t.back(size)

    t.rt(angle)
    t.back(size)

def triangle_frac(t, size, level  = 0):
    if size < 40:
        triangle(t, size)
        return
    # if level == 0:
    #     triangle(t, size)

    triangle_frac(t, size / 2, level + 1)

    t.fd(size / 2)
    triangle_frac(t, size / 2, level + 1)
    t.back(size / 2)

    t.lt(60)
    t.fd(size / 2)
    t.rt(60)

    triangle_frac(t, size / 2, level + 1)
    t.lt(60)
    t.back(size / 2)
    t.rt(60)

def triangle(t, size):
    t.color(random_color())
    for _ in range(3):
        t.fd(size)
        t.lt(120)

tree_levels = [random_color()]
main()
mainloop()
