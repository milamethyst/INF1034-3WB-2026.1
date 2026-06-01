from pygame import *

init()
window = display.set_mode((780, 600))
running = True
clock = time.Clock()
tile_size = 60

mapa = ['GGGGGGGGGGGGG', 'AAAAAAAAAAAAA', 'PPPPPPPPPPPPP', 'GAPGAPGAPGAPG', 'GGGGGAAAAAAPP']

while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False

    clock.tick(60)
    dt = clock.get_time()
    
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == 'G':
                window.blit()
            if mapa[i][j] == 'A':
                draw.rect(window, (230, 235, 134), (tile_size * j, tile_size * i, tile_size, tile_size))
            if mapa[i][j] == 'P':
                draw.rect(window, (63, 125, 232), (tile_size * j, tile_size * i, tile_size, tile_size))

    display.update()