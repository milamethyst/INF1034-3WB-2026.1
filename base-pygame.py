from pygame import *
import sys

init()

window = display.set_mode((1280, 720))


while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

    display.update()