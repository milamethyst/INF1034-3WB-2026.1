from turtle import *
from time import sleep

t = Turtle()

t.speed(0)

t.pu()
t.goto(0, 100)
t.color('black')
t.fillcolor('black')
t.begin_fill()
for side in range(5):
    t.fd(100)
    t.rt(144)
t.end_fill()