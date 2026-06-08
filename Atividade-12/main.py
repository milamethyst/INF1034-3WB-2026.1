from pygame import *

init()

largura_tela = 780
window = display.set_mode((largura_tela, 576))

running = True
clock = time.Clock()

# variáveis iniciais
tile_size = 32
largura_mapa = 1696
hare_x, hare_y = 150, 390
hare_frame = 0
hare_anim_time = 0
cachoeira_frame = 0
cachoeira_anim_time = 0
right = True
velocidade_y = 1
gravidade = 1
no_chao = True
collider_jogador = Rect(hare_x + 20, hare_y + 10, 24, 44)

# coelho
hare_walk = image.load("./Atividade-11/spritesheets/Hare_Walk.png")
hare_walk = transform.scale(hare_walk, (320, 256))
hare_jump = image.load("./Atividade-11/spritesheets/Hare_Run.png")
hare_jump = transform.scale(hare_jump, (384, 256))

# tileset e fundo
tileset = image.load("./Atividade-12/Assets/Floor Tiles1.png")
bg_frente = image.load("./Atividade-12/Assets/BG layer 1.png")
bg_frente = transform.scale(bg_frente, (1696, 576))
bg_fundo = image.load("./Atividade-12/Assets/BG layer 5.png")
bg_fundo = transform.scale(bg_fundo, (1696, 576))
cachoeira = image.load("./Atividade-12/Assets/Animated Water Tiles.png")

# arquivo com o mapa
arq = open('./Atividade-12/Assets/Mapa.txt', 'r')
mapa = []
for linha in arq:
    mapa.append(linha.strip('.\n'))
arq.close()

# dicionário com a relação das letras do mapa com a posição do tileset
tiles = {
    # topo
    'L': (0, 0),  # canto esquerdo
    'T': (1, 0),  # meio
    'R': (2, 0),  # canto direito
    # meio
    'l': (0, 1),  # canto esquerdo
    'M': (1, 1),  # meio
    'r': (2, 1),  # canto direito
    # fundo
    'E': (0, 2),  # canto esquerdo
    'F': (1, 2),  # meio
    'D': (2, 2),  # canto direito
    # partes de baixo das paredes
    'e': (5, 5),
    'd': (4, 5),
    # plataforma
    'p': (6, 5),  # plataforma esquerda
    'P': (7, 5),  # plataforma meio
    'q': (8, 5),  # plataforma direita
}

# função pra checar colisão (pra poder chamar mais de uma vez no loop sem poluir o código)
def checar_colisao(mapa, collider_jogador, tiles, tile_size):
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] in tiles:
                collider_tile = Rect(j * tile_size, i * tile_size, 32, 32)
                if collider_jogador.colliderect(collider_tile):
                    return True
    return False


while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False
        if ev.type == KEYDOWN:
            if (ev.key == K_UP or ev.key == K_w or ev.key == K_SPACE) and no_chao:
                velocidade_y = -15
                no_chao = False

    # variáveis do loop
    keys = key.get_pressed()
    clock.tick(60)
    dt = clock.get_time()
    old_hare_x = hare_x
    old_hare_y = hare_y

    # movimentação
    hare_moving = False

    if keys[K_LEFT] or keys[K_a]:
        right = False
        hare_moving = True
        hare_x -= 3
    if keys[K_RIGHT] or keys[K_d]:
        right = True
        hare_moving = True
        hare_x += 3

    # colisão com parede
    collider_jogador = Rect(hare_x + 20, hare_y + 10, 24, 44)
    if checar_colisao(mapa, collider_jogador, tiles, tile_size):
        hare_x = old_hare_x

    # lógica de pulo
    velocidade_y += gravidade
    hare_y += velocidade_y
    if not no_chao:
        if velocidade_y < -5:
            curr_hare_frame = 2  # subindo
        elif velocidade_y < 0:
            curr_hare_frame = 3  # subindo
        elif velocidade_y <= 2:
            curr_hare_frame = 4  # auge
        else:
            curr_hare_frame = 5  # descendo
        hare = hare_jump
    else:
        if hare_moving:
            hare_anim_time += dt
            if hare_anim_time / 1000 > 0.1:
                hare_frame = (hare_frame + 1) % 5
                hare_anim_time = 0
        else:
            hare_frame = 0
        hare = hare_walk
        curr_hare_frame = hare_frame


    collider_jogador = Rect(hare_x + 20, hare_y + 10, 24, 44)
    if checar_colisao(mapa, collider_jogador, tiles, tile_size):
        hare_y = old_hare_y
        velocidade_y = 0
        no_chao = True

    if right:
        row = 3
    else:
        row = 2

    if hare_x < 0:
        hare_x = 0
    if hare_x > largura_mapa - 64:
        hare_x = largura_mapa - 64

    camera_x = hare_x - largura_tela // 2
    camera_x = max(0, camera_x) 
    camera_x = min(camera_x, largura_mapa - largura_tela)

    window.blit(bg_fundo, (0 - camera_x, 0))
    window.blit(bg_frente, (0 - camera_x, 0))

    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] in tiles:
                col, lin = tiles[mapa[i][j]]
                area = Rect(col * tile_size, lin * tile_size, tile_size, tile_size)
                window.blit(tileset, (j * tile_size - camera_x, i * tile_size), area)
                collider_tile = Rect(j * tile_size, i * tile_size, 32, 32)

    # cachoeira
    cachoeira_x = largura_mapa - 32 - camera_x 
    collider_borda = Rect(cachoeira_x + camera_x - 56, 14 * 32 + 8, 16, 32)
    if collider_jogador.colliderect(collider_borda):
        if hare_x < old_hare_x:
            hare_x = old_hare_x
        else:
            hare_x = old_hare_x + 1
    cachoeira_anim_time += dt
    if cachoeira_anim_time / 1000 > 0.05:
        cachoeira_frame = (cachoeira_frame + 1) % 20
        cachoeira_anim_time = 0

    # blit coelho
    window.blit(hare, (hare_x - camera_x, hare_y), (64 * curr_hare_frame, 64 * row, 64, 64))

    # borda
    window.blit(cachoeira, (cachoeira_x - 64, 14 * 32), (32 * cachoeira_frame, 0, 32, 32))
    # meio
    window.blit(cachoeira, (cachoeira_x - 32, 14 * 32), (32 * cachoeira_frame, 64, 32, 32))
    # cascata
    for k in range(4):
        window.blit(cachoeira, (cachoeira_x, (11 + k) * 32), (32 * cachoeira_frame, 96 + 32 * k, 32, 32))


    display.update()