from pygame import *
import sys

init()

batman_logo = image.load("./Atividade-5/batman.png")
batman_logo = transform.scale(batman_logo, (120, 120))
batman_pixel = image.load("./Atividade-5/batman-pixel.png")
batman_pixel = transform.scale(batman_pixel, (150, 150))

batman_font = font.Font("./Atividade-5/batmfa__.ttf")

# mixer.music.load() # check myinstants website
# mixer.music.play(-1)

window = display.set_mode((1280, 720))

window.fill((151, 209, 250))

while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

    # Casa
    draw.rect(window, (72, 157, 37), (0, 600, 1280, 120)) # chão
    draw.rect(window, (100, 100, 100), (320, 360, 240, 240)) # casa
    draw.rect(window, (13, 22, 100), (350, 456, 60, 96)) # janela
    draw.rect(window, (121, 77, 27), (450, 440, 80, 160)) # porta
    draw.polygon(window, (242, 136, 59), ((300, 360), (440, 240), (580, 360)))
    draw.circle(window, (0, 0, 0), (460, 520), 5)

    # Sol
    # draw.line(window, (255, 242, 81), (50, 50), (150, 150), 6)

    # Imagem
    window.blit(batman_logo, (380, 260))
    window.blit(batman_pixel, (50, 460))
    batman_text = batman_font.render("Even Batman needs to rest sometimes", True, (0, 0, 0))
    window.blit(batman_text, (600, 200))

    display.update()

    # 320, 320, 