from pygame import *
from random import randint
import sys

init()

running = True

window = display.set_mode((1280, 720))

# variáveis
tela = 0

num = ''

listas = [[randint(100, 300) for _ in range(50)], [100, 120, 130, 120, 150, 100, 160, 200, 190, 110, 115, 125, 135, 170, 130], []]

num_cat = 4

info_listas = [[], [], []] # num_min, num_max, tam_cat

lista_total = [[], [], []]
cores = [[], [], []]

fonte_mini = font.SysFont("Arial", 15)
fonte_menor = font.SysFont("Arial", 20)
fonte = font.SysFont("Arial", 30)

def calcula_mins_maxs(id):
    num_min = min(listas[id])
    num_max = max(listas[id])
    if num_max == num_min:
        num_min = 0
    tam_cat = (num_max - num_min) / num_cat

    info_listas[id].append(num_min)
    info_listas[id].append(num_max)
    info_listas[id].append(tam_cat)
    info_listas[id].append([[], [], [], []])
    lista_total[id] = [0] * num_cat

    for i_cat in range(num_cat):
        # obtém os limites inferior e superior
        lim_inf = info_listas[id][0] + i_cat * info_listas[id][2]
        lim_sup = lim_inf + info_listas[id][2]

        info_listas[id][3][i_cat] = [lim_inf, lim_sup]
        

def contabiliza_totais(id):
    calcula_mins_maxs(id)
    # para cada número na lista
    for i in range(len(listas[id])):
        if listas[id][i] == info_listas[id][1]:
            lista_total[id][-1] += 1
            continue

        # para cada faixa/categoria
        for i_cat in range(num_cat):
            # obtém os limites inferior e superior
            lim_inf = info_listas[id][0] + i_cat * info_listas[id][2]
            lim_sup = lim_inf + info_listas[id][2]

            # checa em qual faixa/categoria o número está com base nesses limites
            if lim_inf <= listas[id][i] < lim_sup:
                lista_total[id][i_cat] += 1
                break

def linha_pontilhada(y):
    for i in range(0, 980, 36):
        draw.line(window, '#FFFFFF', (190 + i, y), (190 + i + 10, y))

def desenha(id):
    lista = lista_total[id]
    maximo = max(lista)
    
    pontilhadas = []
    escalas = []

    for fracao in [0.25, 0.5, 0.75, 1]:
        valor = round(maximo * fracao)
        # evita repetir valores iguais
        if valor not in escalas:
            escalas.append(valor)

    for valor in escalas:
        h = 380 / maximo * valor
        y = 500 - h

        draw.line(window, '#FFFFFF', (180, y), (1160, y), 1)

        texto = fonte_menor.render(str(valor), True, '#AAAAAA')
        window.blit(texto, (150, y - 10))
        
    for i in range(len(lista)):
        x = 250 + i * (980 // len(lista))
        h = 380 / maximo * lista[i]
        y = 500 - h
        if cores[id] == []:
            encher_lista_cores(id, len(lista))
        draw.rect(window, cores[id][i], (x, y, (1080 // (len(lista) * 2)), h))

        pontilhadas.append(y)

        write_text = fonte_menor.render(f'{info_listas[id][3][i][0]} - {info_listas[id][3][i][1]}', True, '#FFFFFF')
        text_rect = write_text.get_rect(center=(x + (1080 // (len(lista) * 2)) / 2, 520))
        window.blit(write_text, text_rect)

        write_text = fonte_mini.render(str(lista[i]), True, '#FFFFFF')
        text_rect = write_text.get_rect(center=(1200, y))
        window.blit(write_text, text_rect)

    for y in pontilhadas:
        linha_pontilhada(y)


def encher_lista_cores(id_lista, tamanho):
    for _ in range(tamanho):
        cores[id_lista].append(random_color())
        
def random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def tela_geral(tela):
    window.fill('#000000')
    draw.circle(window, '#FFFFFF', (30, 360), 20, 1)
    draw.circle(window, '#FFFFFF', (1250, 360), 20, 1)

    draw.line(window, '#FFFFFF', (15, 360), (35, 345), 2)
    draw.line(window, '#FFFFFF', (15, 360), (35, 375), 2)
    draw.line(window, '#FFFFFF', (1265, 360), (1245, 345), 2)
    draw.line(window, '#FFFFFF', (1265, 360), (1245, 375), 2)

    if tela == 2:
        draw.rect(window, '#FFFFFF', (570, 600, 140, 50), 2)
        write_text = fonte.render(num, True, '#FFFFFF')
        text_rect = write_text.get_rect(center=(640, 625))
        window.blit(write_text, text_rect)

    if len(listas[tela]) > 0:
        desenha(tela)

    draw.line(window, '#FFFFFF', (100, 500), (1180, 500), 2)
    draw.line(window, '#FFFFFF', (200, 500), (200, 100), 2)


contabiliza_totais(0)
contabiliza_totais(1)

while running:
    x, y = mouse.get_pos()

    for ev in event.get():
        if ev.type == QUIT:
            running = False

        if ev.type == MOUSEBUTTONDOWN:
            if ev.button == 1:
                if (10 <= x <= 50 and 340 <= y <= 380):
                    if tela == 0:
                        tela = 2
                    else:
                        tela -= 1
                elif (1230 <= x <= 1270 and 340 <= y <= 380):
                    if tela == 2:
                        tela = 0
                    else:
                        tela += 1

        if ev.type == KEYDOWN:
            if ev.key == K_BACKSPACE:
                num = num[:-1]
            elif ev.key == K_RETURN:
                listas[2].append(float(num))
                num = ''
                info_listas[2] = []
                lista_total[2] = []
                contabiliza_totais(2)
            elif ev.unicode.isdigit():
                num += ev.unicode


    tela_geral(tela)

    display.update()