from turtle import *
from time import sleep
from math import sqrt

t = Turtle()
t.speed(0)

def main():
    # y = √x
    plano_cartesiano()
    t.color('red')

    t.pu()
    x = 0
    y = func1(x / 50) * 10
    t.goto(x, y)
    t.pd()
    for x in range(1, 301):
        y = func1(x)
        t.goto(x, y)
    sleep(2)
    t.clear()

    # y = 1/x
    plano_cartesiano()
    t.color('red')

    t.pu()
    x = -300
    y = func2(x / 50) * 10
    t.goto(x, y)
    t.pd()
    for x in range(-299, 0):
        y = func2(x/50) * 10
        t.goto(x, y) 

    t.pu()
    x = 1
    y = func2(x / 50) * 10
    t.goto(x, y)
    t.pd()
    for x in range(2, 301):
        y = func2(x/50) * 10
        t.goto(x, y) 
    sleep(2)
    t.clear()

    # y = 2^x
    plano_cartesiano()
    t.color('red')

    t.pu()
    x = -100
    y = func3(x)
    t.goto(x * 3, y)
    t.pd()
    for x in range(-99, 101):
        y = func3(x)
        t.goto(x * 3, y)
    sleep(2)
    t.clear()

    # y = 5 - x^2
    plano_cartesiano()
    t.color('red')

    t.pu()
    x = -100
    y = func4(x)
    t.goto(x, y)
    t.pd()
    for x in range(-99, 101):
        y = func4(x)
        t.goto(x * 3, y * 3)
    sleep(2)
    t.clear()


    # y = x^2 - 5x + 6
    plano_cartesiano()
    t.color('red')
    
    t.pu()
    x = -100
    y = func5(x)
    t.goto(x, y)
    t.pd()

    for x in range(-99, 101):
        y = func5(x)
        t.goto(x * 3, y * 3)
    sleep(2)
    t.clear()


    # y = x^3 - x^2 - x + 1
    plano_cartesiano()

    t.pu()
    x = -100
    y = func6(x)
    t.goto(x, y)
    t.pd()
    t.color('red')
    for x in range(-99, 101):
        y = func6(x)
        t.goto(x * 3, y * 3)
    sleep(2)
    t.clear()
    

def plano_cartesiano():
    t.color('black')

    t.pu()
    t.goto(0, -300)
    t.pd()
    t.goto(0, 300)
    t.lt(90)
    t.stamp()

    t.pu()
    t.goto(-450, 0)
    t.pd()
    t.goto(450, 0)
    t.setheading(0)
    t.stamp()


# y = √x (função 1)
def func1(x):
    y = sqrt(x)
    return y

# y = 1/x (função 2)
def func2(x):
    y = 1/x
    return y

# y = 2^x (função 3)
def func3(x):
    y = 2 ** x
    return y

# y = 5 - x^2 (função 4)
def func4(x):
    y = 5 - (x ** 2)
    return y

# y = x^2 - 5x + 6 (função 5)
def func5(x):
    y = (x ** 2) - (5 * x) + 6
    return y 

# y = x^3 - x^2 - x + 1 (função 6)
def func6(x):
    y = (x ** 3) - (x ** 2) - x + 1
    return y

main()
mainloop()