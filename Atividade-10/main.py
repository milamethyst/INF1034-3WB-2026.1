from pygame import *
from random import randint
import sys

nums = [100, 120, 130, 120, 150, 100, 160, 200, 190, 110, 115, 125, 135, 170, 130]

num_cat = 4
num_min = min(nums)
num_max = max(nums)
tam_cat = (num_max - num_min) / num_cat
lista_total = [0] * num_cat

def contabiliza_totais(nums, lista_total):
    # para cada número na lista
    for i in range(len(nums)):
        if nums[i] == num_max:
            lista_total[-1] += 1
            continue

        # para cada faixa/categoria
        for i_cat in range(num_cat):
            # obtém os limites inferior e superior
            lim_inf = num_min + i_cat * tam_cat
            lim_sup = lim_inf + tam_cat

            # checa em qual faixa/categoria o número está com base nesses limites
            if lim_inf <= nums[i] < lim_sup:
                lista_total[i_cat] += 1
                break
    return lista_total

def desenha(screen):
    screen_h = screen.get_height()
    for i in range(len(lista_total)):
        x = 100 + i * 50
        h = 20 * lista_total[i]
        draw.rect(screen, random_color(), (x, screen_h - h, 25, h))

        
def random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))