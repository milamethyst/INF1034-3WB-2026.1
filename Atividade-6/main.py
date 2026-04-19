from pygame import *

init()
window = display.set_mode((1280, 720))
running = True
clock = time.Clock()

# Fonts and sounds
font = font.Font("./Atividade-6/avatar-font.otf", 40)
sfx_morning = mixer.Sound("./Atividade-6/bird-chirping.mp3")
sfx_afternoon = mixer.Sound("./Atividade-6/wind-chime.mp3")
sfx_night = mixer.Sound("./Atividade-6/owl-hoot.mp3")

# Colors
day = Color(16, 198, 229)
afternoon = Color(236, 174, 121)
night = Color(0, 39, 89)
sea = (64, 127, 204)
sun = (248, 228, 143)
moon = (229, 229, 229)
cloud = (202, 204, 207)

# Variables
cloud_x = 800
cloud_direction = 'right'
sun_x = 500
sun_y = 100
bg_color = day
text = 'Daytime in Pandora'


while running:
    clock.tick(60)

    for ev in event.get():
        if ev.type == QUIT:
            running = False
        if ev.type == MOUSEBUTTONDOWN:
            if ev.button == 1:
                if bg_color == day:
                    sfx_morning.play()
                elif bg_color == afternoon:
                    sfx_afternoon.play()
                else:
                    sfx_night.play()
            
    # Update
    dt = clock.get_time()/1000

    # Sun position
    keys = key.get_pressed()

    if mouse.get_focused() == False:
        if keys[K_d] or keys[K_RIGHT]:
            sun_x = sun_x + 100 * dt
        elif keys[K_a] or keys[K_LEFT]:
            sun_x = sun_x - 100 * dt
        if keys[K_w] or keys[K_UP]:
            sun_y = sun_y - 100 * dt
        elif keys[K_s] or keys[K_DOWN]:
            sun_y = sun_y + 100 * dt
    else:
        sun_x, sun_y = mouse.get_pos()

    # Draw stuff
    window.fill(bg_color)   

    # Sun / moon
    # Not letting it out of bounds
    if sun_y < 90:
        sun_y = 90
    if sun_y > 630:
        sun_y = 630
    if sun_x > 1140:
        sun_x = 1140
    if sun_x < 40:
        sun_x = 40
    
    # BG color (based on sun/moon position)
    if sun_y < 300:
        bg_color = day.lerp(afternoon, (sun_y-90)/300)
        text = 'Daytime in Pandora'
    else:
        bg_color = afternoon.lerp(night, (sun_y-250)/420)
        if sun_y < 550:
            text = 'Afternoon in Pandora'
        else:
            text = 'Nighttime in Pandora'

    if sun_y < 550:
        draw.line(window, sun, (sun_x+50, sun_y-90), (sun_x+50, sun_y+90), 3) # top-bottom
        draw.line(window, sun, (sun_x-40, sun_y), (sun_x+140, sun_y), 3) # left-right
        draw.line(window, sun, (sun_x-5, sun_y-55), (sun_x+105, sun_y+55), 2) # top+left-bottom+right
        draw.line(window, sun, (sun_x-5, sun_y+55), (sun_x+105, sun_y-55), 2) # bottom+left-top+right
        draw.circle(window, sun, (sun_x+50, sun_y), 50) # circle
    else:
        draw.circle(window, moon, (sun_x+50, sun_y), 50)

    # Sea
    draw.rect(window, sea, (0, 600, 1280, 120))
    
    # Cloud
    draw.circle(window, cloud, (cloud_x+50, 150), 50)
    draw.circle(window, cloud, (cloud_x+120, 150), 65)
    draw.circle(window, cloud, (cloud_x+190, 150), 65)
    draw.circle(window, cloud, (cloud_x+260, 150), 50)

    if cloud_direction == 'right':
        cloud_x = cloud_x + 100 * dt
        if cloud_x > 970:
            cloud_direction = 'left'
    elif cloud_direction == 'left':
        cloud_x = cloud_x - 100 * dt
        if cloud_x < 0:
            cloud_direction = 'right'

    # House
    draw.rect(window, (187, 116, 86), (320, 360, 240, 240)) # house
    draw.rect(window, (160, 97, 54), (350, 456, 60, 96)) # window
    draw.rect(window, (160, 97, 54), (450, 440, 80, 160)) # door
    draw.polygon(window, (188, 66, 7), ((300, 360), (440, 240), (580, 360))) # top

    write_text = font.render(text, True, (255, 255, 255))
    window.blit(write_text, (700, 260))

    display.update()