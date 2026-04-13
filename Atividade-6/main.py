from pygame import *

init()
window = display.set_mode((1280, 720))
running = True
clock = time.Clock()


# Variáveis
pos_x = 0

while running:
    clock.tick(60)

    for ev in event.get():
        if ev.type == QUIT:
            running = False

    dt = clock.get_time()/1000


    display.update()