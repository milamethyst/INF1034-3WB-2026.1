from pygame import *
import sys

init()

batman_logo = image.load("./Atividade-5/batman-logo.png")
batman_logo = transform.scale(batman_logo, (140, 140))
batman = image.load("./Atividade-5/batman.png")
batman = transform.scale(batman, (80, 178))

batman_font = font.Font("./Atividade-5/batman-noir-font.otf", 40)

mixer.music.load("./Atividade-5/something-in-the-way-the-batman.mp3")
mixer.music.play(-1)

window = display.set_mode((1280, 720))

window.fill((31, 51, 130))

x = 50

while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

    # Casa
    window.fill((31, 51, 130))
    draw.rect(window, (2, 64, 0), (0, 600, 1280, 120)) # chão
    draw.rect(window, (100, 100, 100), (320, 360, 240, 240)) # casa
    draw.rect(window, (201, 165, 34), (350, 456, 60, 96)) # janela
    draw.rect(window, (56, 56, 56), (450, 440, 80, 160)) # porta
    draw.polygon(window, (0, 0, 0), ((300, 360), (440, 240), (580, 360)))
    draw.circle(window, (0, 0, 0), (460, 520), 5)

    # Árvore
    draw.rect(window, (84, 41, 3), (960, 400, 80, 200)) # tronco
    draw.circle(window, (0, 48, 2), (1000, 350), 90)

    # Lua
    draw.circle(window, (140, 178, 194), (200, 150), 100)
    draw.circle(window, (31, 51, 130), (230, 150), 100)

    # Nuvem
    def nuvem(x, y, size):
        for i in range(2):
            draw.circle(window, (164, 174, 179), (x+i*(size + 10)*3, y), size)
        for i in range(2):
            draw.circle(window, (164, 174, 179), (x+50+i*(size + 10), y), size+10)

    nuvem(900, 100, 50)
    nuvem(600, 150, 35)

    # Linhas
    draw.line(window, (0, 0, 0), (650, 500), (650, 600), 3)
    draw.line(window, (0, 0, 0), (770, 500), (770, 600), 3)

    # Imagem
    window.blit(batman_logo, (640, 430))
    batman_text = batman_font.render("Even Batman needs to rest sometimes", True, (0, 0, 0))
    window.blit(batman_text, (600, 220))

    window.blit(batman, (x, 450))
    x = x + 0.064

    if x > 450:
        x = 50

    display.update()