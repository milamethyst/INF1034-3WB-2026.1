from pygame import *

init()

running = True

window = display.set_mode((1280, 720))

palavras_comida = ['arroz', 'banana', 'queijo', 'alface', 'frango']
texto_usuario = ''

def desenhar_forca(erros):
    # forca


    if erros >= 1:
        # cabeça
        print("cabeça")
    if erros >= 2:
        # torso
        print("torso")
    if erros >= 3:
        # braço 1
        print("braço 1")
    if erros >= 4:
        # braço 2
        print("braço 2")
    if erros >= 5:
        # perna 1
        print("perna 1")
    if erros >= 6:
        # perna 2
        print("perna 2")

while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False



    display.update()