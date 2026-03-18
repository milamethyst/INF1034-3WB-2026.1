from turtle import *

t = Turtle()

x = 300

# Desenhando o plano cartesiano
t.pu()
t.goto(0, -500)
t.pd()
t.lt(90)
t.fd(1000)
t.pu()
t.goto(-1000, 0)
t.pd()
t.rt(90)
t.fd(2000)


# Desenhando um triângulo
t.pu()
t.goto(x, x)
t.pd()
color = textinput("Obter cor", "Digite uma cor para o triângulo")
t.color(color)
t.begin_fill()
for _ in range(3):
    t.fd(100)
    t.lt(120)
t.end_fill()

# Desenhando um hexágono
t.pu()
t.goto(x, -x)
t.pd()
color = textinput("Obter cor", "Digite uma cor para o hexágono")
t.color(color)
t.begin_fill()
for _ in range(6):
    t.fd(75)
    t.lt(60)
t.end_fill()

# Desenhando um octógono
t.pu()
t.goto(-x, -x)
t.pd()
color = textinput("Obter cor", "Digite uma cor para o octógono")
t.color(color)
t.begin_fill()
for _ in range(8):
    t.fd(75)
    t.lt(45)
t.end_fill()

# Desenhando uma estrela
t.pu()
t.goto(-x, x)
t.pd()
color = textinput("Obter cor", "Digite uma cor para a estrela")
t.color(color)
t.begin_fill()
for _ in range(6):
    t.fd(150)
    t.lt(144)
t.end_fill()

# Desenhando uma espiral
t.pu()
t.goto(2.5*x, x)
t.pd()
color = textinput("Obter cor", "Digite uma cor para a espiral")
t.color(color)
for i in range(75):
    t.fd(i * 1.25)
    t.lt(30)


mainloop()