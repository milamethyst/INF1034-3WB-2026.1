from pygame import *
from random import choice, randint

init()
window = display.set_mode((1280, 720))
running = True
clock = time.Clock()


# cores
muito_escuro = Color(41, 0, 33)
escuro = Color(61, 0, 50)
medio_escuro = Color(163, 0, 133)
medio = Color(255, 175, 240)
medio_claro = Color(255, 214, 247)
claro = Color(255, 235, 251)
muito_claro = Color(255, 243, 253)

botao = Color(224, 190, 218)
botao_apertado = Color(163, 92, 150)


# imagens
forca = image.load("./Atividade-7/Recursos/Botões/forca.png")
forca = transform.scale(forca, (200, 200))
ppt = image.load("./Atividade-7/Recursos/Botões/pedra-papel-tesoura.png")
ppt = transform.scale(ppt, (200, 200))
calculadora = image.load("./Atividade-7/Recursos/Botões/calculadora.png")
calculadora = transform.scale(calculadora, (200, 200))
adivinhacao = image.load("./Atividade-7/Recursos/Botões/adivinhação.png")
adivinhacao = transform.scale(adivinhacao, (200, 200))

comida = image.load("./Atividade-7/Recursos/Botões/Temas Forca/comida.png")
comida = transform.scale(comida, (200, 200))
jogos = image.load("./Atividade-7/Recursos/Botões/Temas Forca/jogos.png")
jogos = transform.scale(jogos, (200, 200))
pokemon = image.load("./Atividade-7/Recursos/Botões/Temas Forca/pokemon.png")
pokemon = transform.scale(pokemon, (200, 200))
star_wars = image.load("./Atividade-7/Recursos/Botões/Temas Forca/star wars.png")
star_wars = transform.scale(star_wars, (200, 200))

font = font.Font("./Atividade-7/Recursos/Outros/font.otf", 120)


# variáveis
jogo = 'menu'
texto_usuario = ''
erros = 0
tema = ''

# listas palavras
palavras_comida = ['arroz', 'banana', 'queijo', 'alface', 'frango', 'amendoim', 'chocolate', 'pepino', 'batata', 'couve', 'carne']
palavras_jogos = ['controle', 'steam', 'playstation', 'xbox', 'nintendo', 'overwatch', 'valorant', 'console', 'minecraft', 'computador', 'mouse', 'teclado', 'ranqueada', 'genshin', 'atari', 'gameboy', 'overcooked', 'fortnite', 'undertale', 'deltarune', 'bloons', 'megabonk', 'peak', 'spiritfarer']
palavras_pokemon = ['pikachu', 'wooper', 'quagsire', 'oshawott', 'piplup', 'lucario', 'bulbasaur', 'ivysaur', 'venusaur', 'charmander', 'charmeleon', 'charizard', 'squirtle', 'wartortle', 'blastoise', 'caterpie', 'metapod', 'butterfree', 'weedle', 'kakuna', 'beedrill', 'pidgey', 'pidgeotto', 'pidgeot', 'rattata', 'raichu', 'vaporeon', 'jolteon', 'flareon', 'espeon', 'umbreon', 'leafeon', 'glaceon', 'sylveon', 'eevee', 'clefairy', 'clefable', 'vulpix', 'ninetales', 'zubat', 'jigglypuff', 'meowth']
palavras_starwars = ['skywalker', 'vader', 'jedi', 'anakin', 'sith', 'yoga']

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

def botoes(modo):
    if modo == 'menu':
        write_text = font.render('jogos!', True, medio_escuro)
        window.blit(write_text, (520, 0))
        draw.rect(window, botao, (60, 100, 560, 280), 0, 20)
        window.blit(forca, (240, 140))
        draw.rect(window, botao, (660, 100, 560, 280), 0, 20)
        window.blit(ppt, (840, 140))
        draw.rect(window, botao, (60, 420, 560, 280), 0, 20)
        window.blit(calculadora, (240, 460))
        draw.rect(window, botao, (660, 420, 560, 280), 0, 20)
        window.blit(adivinhacao, (840, 460))

    elif modo == 'ppt':
        draw.rect(window)

    elif modo == 'forca':
        write_text = font.render('temas!', True, medio_escuro)
        window.blit(write_text, (520, 0))
        draw.rect(window, botao, (60, 100, 560, 280), 0, 20)
        window.blit(comida, (240, 140))
        draw.rect(window, botao, (660, 100, 560, 280), 0, 20)
        window.blit(jogos, (840, 140))
        draw.rect(window, botao, (60, 420, 560, 280), 0, 20)
        window.blit(pokemon, (240, 460))
        draw.rect(window, botao, (660, 420, 560, 280), 0, 20)
        window.blit(star_wars, (840, 460))


while running:
    clock.tick(60)
    x, y = mouse.get_pos()

    for ev in event.get():
        if ev.type == QUIT:
            running = False
        if ev.type == MOUSEBUTTONDOWN:
            if ev.button == 1:
                match jogo:
                    case 'menu':
                        if (60 <= x <= 620 and 100 <= y <= 380):
                            jogo = 'forca'
                        elif (660 <= x <= 1220 and 100 <= y <= 380):
                            jogo = 'ppt'
                        elif (60 <= x <= 620 and 420 <= y <= 700):
                            jogo = 'calc'
                        elif (660 <= x <= 1220 and 420 <= y <= 700):
                            jogo = 'adiv'
                    case 'forca':
                        if (60 <= x <= 620 and 100 <= y <= 380):
                            tema = 'comida'
                        elif (660 <= x <= 1220 and 100 <= y <= 380):
                            tema = 'jogos'
                        elif (60 <= x <= 620 and 420 <= y <= 700):
                            tema = 'pokemon'
                        elif (660 <= x <= 1220 and 420 <= y <= 700):
                            tema = 'star wars'                
    

    window.fill(muito_claro)   

    match jogo:
        case 'forca':
            if tema == '':
                botoes('forca')
            else:
                match tema:
                    case 'comida':
                        palavra = choice(palavras_comida)
                    case 'jogos':
                        palavra = choice()
            #palavra = choice(palavras_comida)
            #desenhar_forca(erros)
        case 'ppt':
            botoes('ppt')
        case 'calc':
            botoes('calc')
        case 'adiv':
            botoes('adiv')
        case default:
            botoes('menu')

    display.update()