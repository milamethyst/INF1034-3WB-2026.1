from pygame import *
from random import choice, randint

init()

running = True

window = display.set_mode((1280, 720))

palavras_comida = ['arroz', 'banana', 'queijo', 'alface', 'frango']
jogo = ''
texto_usuario = ''
erros = 0

def desenhar_forca(erros):
    # forca
    draw.line(window, (0, 0, 0), (175, 600), (225, 600), 4)
    draw.line(window, (0, 0, 0), (200, 600), (200, 300), 4)
    draw.line(window, (0, 0, 0), (200, 300), (300, 300), 4)
    draw.line(window, (0, 0, 0), (300, 300), (300, 350), 4)

    if erros >= 1:
        draw.circle(window, (0, 0, 0), (300, 370), 20, 2) # cabeça
    if erros >= 2:
        draw.line(window, (0, 0, 0), (300, 390), (300, 450), 2) # torso
    if erros >= 3:
        draw.line(window, (0, 0, 0), (280, 420), (300, 400), 2) # braço 1
    if erros >= 4:
        draw.line(window, (0, 0, 0), (300, 400), (320, 420), 2) # braço 2
    if erros >= 5:
        draw.line(window, (0, 0, 0), (280, 470), (300, 450), 2) # perna 1
    if erros >= 6:
        draw.line(window, (0, 0, 0), (300, 450), (320, 470), 2) # perna 2

def botoes():
    draw.rect(window, (175, 175, 175), (10, 10, 620, 340))
    draw.rect(window, (175, 175, 175), (650, 10, 620, 340))
    draw.rect(window, (175, 175, 175), (10, 370, 620, 340))
    draw.rect(window, (175, 175, 175), (650, 370, 620, 340))


window.fill((255, 255, 255))   

desenhar_forca(6)

while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False

    match jogo:
        case 'forca':
            palavra = choice(palavras_comida)
            desenhar_forca(erros)
        case default:
            botoes()

    display.update()