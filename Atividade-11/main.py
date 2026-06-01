from pygame import *

init()
window = display.set_mode((780, 600))
running = True
clock = time.Clock()

# spritesheets
grouse = image.load("./Atividade-11/spritesheets/Black_grouse_Flight.png")
grouse = transform.scale(grouse, (384, 256))
boar = image.load("./Atividade-11/spritesheets/Boar_Attack.png")
boar = transform.scale(boar, (320, 256))
fox = image.load("./Atividade-11/spritesheets/Fox_Death.png")
fox = transform.scale(fox, (384, 256))
hare = image.load("./Atividade-11/spritesheets/Hare_Walk.png")
hare_jump = image.load("./Atividade-11/spritesheets/Hare_Run.png")

fonte = font.SysFont("Arial", 20)

# variaveis
grouse_pos = 100, 100
button_y = 250
boar_pos = 100, button_y
fox_pos = 160, button_y
hare_x, hare_y = 50, 500

curr_frame_still = 0
anim_time_still = 0

curr_frame_button = 0
anim_time_button = 0
frame_boar = 0
frame_fox = 0

run_animation = False
jump = False
right = True

while running:
    clock.tick(60)
    dt = clock.get_time()
    keys = key.get_pressed()

    for ev in event.get():
        if ev.type == QUIT:
            running = False
        if ev.type == KEYDOWN:
            if ev.key == K_SPACE:
                jump = True
            if ev.key == K_RETURN:
                run_animation = True

    # pássaro voando (constante)
    anim_time_still = anim_time_still + dt
    anim_time_still_sec = anim_time_still/1000

    if anim_time_still_sec > 0.1:
        curr_frame_still += 1
        if curr_frame_still > 5:
            curr_frame_still = 0
        anim_time_still = 0

    # ataque (botão)
    if run_animation:
        anim_time_button = anim_time_button + dt
        anim_time_button_sec = anim_time_button/1000

        if anim_time_button_sec > 0.1:
            curr_frame_button += 1
            if curr_frame_button > 9:
                curr_frame_button = 0
                run_animation = False
            anim_time_button = 0

            frame_fox = curr_frame_button - 1
            frame_boar = curr_frame_button

            if frame_boar > 4:
                frame_boar = 0
            if frame_fox > 5:
                frame_fox = 5
            if frame_fox < 0:
                frame_fox = 0
        
    # movimentação



    print(frame_boar, frame_fox)
    window.fill((255, 255, 255))

    write_text = fonte.render('pressione "Enter" para rodar a animação', True, '#000000')
    text_rect = write_text.get_rect(center=(450, button_y + 32))
    window.blit(write_text, text_rect)
    
    window.blit(grouse, grouse_pos, (64 * (curr_frame_still % 6), 0, 64, 64))
    window.blit(fox, fox_pos, (64 * (frame_fox % 6), 128, 64, 64))
    window.blit(boar, boar_pos, (64 * (frame_boar % 5), 192, 64, 64))

    display.update()