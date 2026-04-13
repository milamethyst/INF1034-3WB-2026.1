from pygame import *

init()
window = display.set_mode((1280, 720))
running = True
clock = time.Clock()


# Variáveis
pos_x = 0
bg_color = '#000000'
text = ''


while running:
    clock.tick(60)
    keys = key.get_pressed()
    mouse_buttons = mouse.get_pressed()

    for ev in event.get():
        if ev.type == QUIT:
            running = False
        if ev.type == KEYDOWN:
            pressed = ev.key
            if pressed == K_SPACE:
                if bg_color == '#000000':
                    bg_color = ((255, 255, 255))
                elif bg_color == (255, 255, 255):
                    bg_color = ('#000000')
        if ev.type == MOUSEBUTTONUP:
            if ev.button == 1:
                text = 'AHAHA'
            

    # Update
    dt = clock.get_time()/1000


    if keys[K_d] or keys[K_RIGHT]:
        pos_X = pos_x + 1 * dt
    elif keys[K_a] or keys[K_LEFT]:
        pos_X = pos_x - 1 * dt

    # Draw
    window.fill(bg_color)


    display.update()