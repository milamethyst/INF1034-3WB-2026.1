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

# imagens
forca = image.load("./Atividade-7/Recursos/Botões/Jogos/forca.png")
forca = transform.scale(forca, (150, 150))
ppt = image.load("./Atividade-7/Recursos/Botões/Jogos/pedra-papel-tesoura.png")
ppt = transform.scale(ppt, (150, 150))
calculadora = image.load("./Atividade-7/Recursos/Botões/Jogos/calculadora.png")
calculadora = transform.scale(calculadora, (150, 150))
adivinhacao = image.load("./Atividade-7/Recursos/Botões/Jogos/adivinhação.png")
adivinhacao = transform.scale(adivinhacao, (150, 150))

comida = image.load("./Atividade-7/Recursos/Botões/Temas Forca/comida.png")
comida = transform.scale(comida, (200, 200))
jogos = image.load("./Atividade-7/Recursos/Botões/Temas Forca/jogos.png")
jogos = transform.scale(jogos, (200, 200))
pokemon = image.load("./Atividade-7/Recursos/Botões/Temas Forca/pokemon.png")
pokemon = transform.scale(pokemon, (200, 200))
star_wars = image.load("./Atividade-7/Recursos/Botões/Temas Forca/star wars.png")
star_wars = transform.scale(star_wars, (200, 200))

pedra = image.load("./Atividade-7/Recursos/Botões/Pedra Papel Tesoura/pedra.png")
pedra = transform.scale(pedra, (300, 300))
papel = image.load("./Atividade-7/Recursos/Botões/Pedra Papel Tesoura/papel.png")
papel = transform.scale(papel, (300, 300))
tesoura = image.load("./Atividade-7/Recursos/Botões/Pedra Papel Tesoura/tesoura.png")
tesoura = transform.scale(tesoura, (300, 300))

jogador = image.load("./Atividade-7/Recursos/Botões/Adivinhação/jogador.png")
jogador = transform.scale(jogador, (300, 300))
computador = image.load("./Atividade-7/Recursos/Botões/Adivinhação/computador.png")
computador = transform.scale(computador, (300, 300))
menor = image.load("./Atividade-7/Recursos/Botões/Adivinhação/menor.png")
menor = transform.scale(menor, (300, 300))
maior = image.load("./Atividade-7/Recursos/Botões/Adivinhação/maior.png")
maior = transform.scale(maior, (300, 300))
venceu = image.load("./Atividade-7/Recursos/Botões/Adivinhação/venceu.png")
venceu = transform.scale(venceu, (300, 300))

img0 = image.load("./Atividade-7/Recursos/Botões/Calculadora/0.png")
img0 = transform.scale(img0, (144, 144))
img1 = image.load("./Atividade-7/Recursos/Botões/Calculadora/1.png")
img1 = transform.scale(img1, (144, 144))
img2 = image.load("./Atividade-7/Recursos/Botões/Calculadora/2.png")
img2 = transform.scale(img2, (144, 144))
img3 = image.load("./Atividade-7/Recursos/Botões/Calculadora/3.png")
img3 = transform.scale(img3, (144, 144))
img4 = image.load("./Atividade-7/Recursos/Botões/Calculadora/4.png")
img4 = transform.scale(img4, (144, 144))
img5 = image.load("./Atividade-7/Recursos/Botões/Calculadora/5.png")
img5 = transform.scale(img5, (144, 144))
img6 = image.load("./Atividade-7/Recursos/Botões/Calculadora/6.png")
img6 = transform.scale(img6, (144, 144))
img7 = image.load("./Atividade-7/Recursos/Botões/Calculadora/7.png")
img7 = transform.scale(img7, (144, 144))
img8 = image.load("./Atividade-7/Recursos/Botões/Calculadora/8.png")
img8 = transform.scale(img8, (144, 144))
img9 = image.load("./Atividade-7/Recursos/Botões/Calculadora/9.png")
img9 = transform.scale(img9, (144, 144))

adicao = image.load("./Atividade-7/Recursos/Botões/Calculadora/adição.png")
adicao = transform.scale(adicao, (144, 144))
divisao = image.load("./Atividade-7/Recursos/Botões/Calculadora/divisão.png")
divisao = transform.scale(divisao, (144, 144))
igual = image.load("./Atividade-7/Recursos/Botões/Calculadora/igual.png")
igual = transform.scale(igual, (144, 144))
multi = image.load("./Atividade-7/Recursos/Botões/Calculadora/multiplicação.png")
multi = transform.scale(multi, (144, 144))
ponto = image.load("./Atividade-7/Recursos/Botões/Calculadora/ponto.png")
ponto = transform.scale(ponto, (144, 144))
sub = image.load("./Atividade-7/Recursos/Botões/Calculadora/subtração.png")
sub = transform.scale(sub, (144, 144))
volta1 = image.load("./Atividade-7/Recursos/Botões/Calculadora/volta1.png")
volta1 = transform.scale(volta1, (144, 144))
volta_tudo = image.load("./Atividade-7/Recursos/Botões/Calculadora/volta-tudo.png")
volta_tudo = transform.scale(volta_tudo, (144, 144))
sair = image.load("./Atividade-7/Recursos/Botões/Calculadora/sair.png")
sair = transform.scale(sair, (144, 144))

fonte = font.Font("./Atividade-7/Recursos/Outros/font.ttf", 100)
fonte_menor = font.Font("./Atividade-7/Recursos/Outros/font.ttf", 60)
fonte_menor_ainda = font.Font("./Atividade-7/Recursos/Outros/font.ttf", 40)
fonte_mini = font.Font("./Atividade-7/Recursos/Outros/font.ttf", 25)

# variáveis
mensagem_voltar = 'pressione enter para jogar de novo ou backspace para voltar'
jogo = 'login'
erros = 0
tema = ''
palavra = ''
palavra_forca = ''
letras_tentadas = []
final = False
pressionado = False
texto = 'Pressione enter após inserir email e senha'
chute = ''
texto_extra = ''
jogada = 0
adivinha = ''
pontos = 0
ppt_computador = 0
num_aleatorio = 0
num_chute = 0
min = 1
max = 1023
tentativas = 1
segunda_linha = ''
num1 = 0
num2 = 0
resultado = 0
opera = ''
email = ''
senha = ''
cripto = ''
inseriu_email = False
inseriu_senha = False
cloud_x = 800
cloud_direction = 'right'
sun_x = 500
sun_y = 100

# listas palavras
palavras_comida = ['arroz', 'banana', 'queijo', 'alface', 'frango', 'amendoim', 'chocolate', 'pepino', 'batata', 'couve', 'carne']
palavras_jogos = ['controle', 'steam', 'playstation', 'xbox', 'nintendo', 'overwatch', 'valorant', 'console', 'minecraft', 'computador', 'mouse', 'teclado', 'ranqueada', 'genshin', 'atari', 'gameboy', 'overcooked', 'fortnite', 'undertale', 'deltarune', 'bloons', 'megabonk', 'peak', 'spiritfarer']
palavras_pokemon = ['pikachu', 'wooper', 'quagsire', 'oshawott', 'piplup', 'lucario', 'bulbasaur', 'ivysaur', 'venusaur', 'charmander', 'charmeleon', 'charizard', 'squirtle', 'wartortle', 'blastoise', 'caterpie', 'metapod', 'butterfree', 'weedle', 'kakuna', 'beedrill', 'pidgey', 'pidgeotto', 'pidgeot', 'rattata', 'raichu', 'vaporeon', 'jolteon', 'flareon', 'espeon', 'umbreon', 'leafeon', 'glaceon', 'sylveon', 'eevee', 'clefairy', 'clefable', 'vulpix', 'ninetales', 'zubat', 'jigglypuff', 'meowth', 'psyduck', 'growlithe', 'arcanine', 'poliwag', 'poliwhirl', 'abra', 'machop', 'weepinbell', 'geodude', 'ponyta', 'slowpoke', 'gengar', 'chansey', 'horsea', 'magikarp', 'gyarados', 'ditto', 'lapras', 'snorlax', 'dragonite', 'chikorita', 'cyndaquil', 'typhlosion', 'totodile', 'togepi', 'mareep']
palavras_starwars = ['skywalker', 'vader', 'jedi', 'anakin', 'sith', 'yoda']

# funções

def valida_email(email):
    return email[-8:] == '@puc.com' # retorna True se o final for @puc.com

def valida_senha(senha):
    return len(senha) >= 8 and tem_maiuscula(senha) and tem_minuscula(senha) and tem_numero(senha) # retorna True apenas se todos os parâmetros são True

def tem_maiuscula(palavra):
    for caracter in palavra:
        if caracter.isupper():
            return True
    return False # retorna False se percorreu toda a string e não encontrou nenhuma maiúscula

def tem_minuscula(palavra):
    for caracter in palavra:
        if caracter.islower():
            return True
    return False # retorna False se percorreu toda a string e não encontrou nenhuma minúscula

def tem_numero(palavra):
    for caracter in palavra:
        if caracter.isdigit():
            return True
    return False # retorna False se percorreu toda a string e não encontrou nenhum número

def codifica_cesar(senha):
    senha_nova = ''
    for caracter in senha:
        if caracter.isdigit() or caracter.isalpha():
            max = 0
            ref = 0
            if caracter.isdigit():
                ref = ord('0')
                max = ord('9')
            elif caracter.islower():
                ref = ord('a')
                max = ord('z')
            elif caracter.isupper():
                ref = ord('A')
                max = ord('Z')
            decimal = ord(caracter) # transforma na posição na tabela ascii
            decimal -= ref # subtrai o valor de referência
            decimal += 3 # adiciona 3
            decimal = decimal % (max - ref + 1) # obtem o resto (do máximo menos a referência + 1)
            decimal += ref # soma o valor de referência
            senha_nova += chr(decimal) # adiciona o caracter novo na senha criptografada
        else:
            senha_nova += caracter # repete se for caracter especial
    return senha_nova

def reverte_cesar(codificado):
    decodificado = ''
    for c in codificado:
        if c.isdigit() or c.isalpha():
            max = 0
            ref = 0
            if c.isdigit():
                ref = ord('0')
                max = ord('9')
            elif c.islower():
                ref = ord('a')
                max = ord('z')
            elif c.isupper():
                ref = ord('A')
                max = ord('Z')
            decimal = ord(c) # transforma na posição na tabela ascii
            decimal -= ref # subtrai o valor de referência
            decimal -= 3 # adiciona 3
            decimal = decimal % (max - ref + 1) # obtem o resto (do máximo menos a referência + 1)
            decimal += ref # soma o valor de referência
            decodificado += chr(decimal) # adiciona o caracter novo na senha criptografada
        else:
            decodificado += c # repete se for caracter especial
    return decodificado

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
        casinha(x, y)
        write_text = fonte.render('jogos!', True, medio_escuro)
        window.blit(write_text, (520, 0))
        draw.rect(window, botao, (10, 510, 300, 200), 0, 20)
        window.blit(forca, (85, 535))
        draw.rect(window, botao, (330, 510, 300, 200), 0, 20)
        window.blit(ppt, (405, 535))
        draw.rect(window, botao, (650, 510, 300, 200), 0, 20)
        window.blit(calculadora, (725, 535))
        draw.rect(window, botao, (970, 510, 300, 200), 0, 20)
        window.blit(adivinhacao, (1045, 535))
        write_text = fonte_mini.render(f'Criptografada: {cripto}', True, medio_escuro)
        window.blit(write_text, (900, 450))
        write_text = fonte_mini.render(f'Descriptografada: {reverte_cesar(cripto)}', True, medio_escuro)
        window.blit(write_text, (900, 480))

    elif modo == 'forca':
        write_text = fonte.render('temas!', True, medio_escuro)
        window.blit(write_text, (520, 0))
        draw.rect(window, botao, (60, 100, 560, 280), 0, 20)
        window.blit(comida, (240, 140))
        draw.rect(window, botao, (660, 100, 560, 280), 0, 20)
        window.blit(jogos, (840, 140))
        draw.rect(window, botao, (60, 420, 560, 280), 0, 20)
        window.blit(pokemon, (240, 460))
        draw.rect(window, botao, (660, 420, 560, 280), 0, 20)
        window.blit(star_wars, (840, 460))

    elif modo == 'ppt':
        draw.rect(window, botao, (60, 60, 360, 600), 0, 20)
        window.blit(pedra, (90, 210))
        draw.rect(window, botao, (460, 60, 360, 600), 0, 20)
        window.blit(papel, (490, 210))
        draw.rect(window, botao, (860, 60, 360, 600), 0, 20)
        window.blit(tesoura, (890, 210))

    elif modo == 'adiv':
        write_text = fonte_menor.render('quem vai adivinhar?', True, medio_escuro)
        window.blit(write_text, (320, 20))
        draw.rect(window, botao, (60, 100, 560, 600), 0, 20)
        window.blit(jogador, (190, 250))
        draw.rect(window, botao, (660, 100, 560, 600), 0, 20)
        window.blit(computador, (790, 250))

    elif modo == 'adiv-comp':
        write_text = fonte_menor.render(f'O computador chutou {num_chute}', True, medio_escuro)
        window.blit(write_text, (250, 20))
        draw.rect(window, botao, (60, 100, 360, 600), 0, 20)
        window.blit(menor, (90, 250))
        draw.rect(window, botao, (460, 100, 360, 600), 0, 20)
        window.blit(venceu, (490, 250))
        draw.rect(window, botao, (860, 100, 360, 600), 0, 20)
        window.blit(maior, (890, 250))

    elif modo == 'calc':
        draw.rect(window, botao, (342, 2, 596, 718), 0, 20)
        draw.rect(window, muito_claro, (350, 10, 580, 120), 0, 15)
        draw.circle(window, claro, (418, 208), 72)
        window.blit(img7, (346, 136)) # 7 -> 346 x 490 , 136 y 280
        draw.circle(window, claro, (566, 208), 72)
        window.blit(img8, (494, 136)) # 8 -> 494 x 638 , 136 y 280
        draw.circle(window, claro, (714, 208), 72)
        window.blit(img9, (642, 136)) # 9 -> 642 x 786 , 136 y 280
        draw.circle(window, claro, (862, 208), 72)
        window.blit(divisao, (790, 136)) # / -> 790 x 934 , 136 y 280
        draw.circle(window, claro, (418, 354), 72)
        window.blit(img4, (346, 282)) # 4 -> 346 x 490 , 282 y 426
        draw.circle(window, claro, (566, 354), 72)
        window.blit(img5, (494, 282)) # 5 -> 494 x 638 , 282 y 426
        draw.circle(window, claro, (714, 354), 72)
        window.blit(img6, (642, 282)) # 6 -> 642 x 786 , 282 y 426
        draw.circle(window, claro, (862, 354), 72)
        window.blit(multi, (790, 282)) # * -> 790 x 934 , 282 y 426
        draw.circle(window, claro, (418, 500), 72)
        window.blit(img1, (346, 428)) # 1 -> 346 x 490 , 428 y 572
        draw.circle(window, claro, (566, 500), 72)
        window.blit(img2, (494, 428)) # 2 -> 494 x 638 , 428 y 572
        draw.circle(window, claro, (714, 500), 72)
        window.blit(img3, (642, 428)) # 3 -> 642 x 786 , 428 y 572
        draw.circle(window, claro, (862, 500), 72)
        window.blit(sub, (790, 428)) # - -> 790 x 934 , 428 y 572
        draw.circle(window, claro, (418, 646), 72)
        window.blit(img0, (346, 574)) # 0 -> 346 x 490 , 574 y 718
        draw.circle(window, claro, (566, 646), 72)
        window.blit(ponto, (494, 574)) # . -> 494 x 638 , 574 y 718
        draw.circle(window, claro, (714, 646), 72)
        window.blit(igual, (642, 574)) # = -> 642 x 786 , 574 y 718
        draw.circle(window, claro, (862, 646), 72)
        window.blit(adicao, (790, 574)) # + -> 790 x 934 , 574 y 718
       
        draw.circle(window, botao, (1110, 230), 72)
        window.blit(volta1, (1038, 158)) # < -> 1038 x 1182 , 158 y 302
        draw.circle(window, botao, (1110, 490), 72)
        window.blit(volta_tudo, (1038, 418)) # << -> 1038 x 1182 , 418 y 562
        
        draw.circle(window, botao, (150, 360), 72)
        window.blit(sair, (78, 288)) # sair -> 78 x 222, 288 y 432

    elif modo == 'login':
        draw.rect(window, medio_claro, (340, 210, 600, 300), 0, 20)
        write_text = fonte_mini.render('Login:', True, muito_escuro)
        window.blit(write_text, (380, 240))
        draw.rect(window, muito_claro, (380, 270, 520, 50))
        write_text = fonte_mini.render('Senha:', True, muito_escuro)
        window.blit(write_text, (380, 360))
        draw.rect(window, muito_claro, (380, 390, 520, 50))
        write_text = fonte_mini.render(texto, True, escuro)
        text_rect = write_text.get_rect(center=(640, 480))
        window.blit(write_text, text_rect)

        write_text = fonte_mini.render(email, True, escuro)
        window.blit(write_text, (385, 290))
        write_text = fonte_mini.render(senha, True, escuro)
        window.blit(write_text, (385, 410))

def casinha(x, y):
    global cloud_x, cloud_direction, sun_x, sun_y
    day = Color(16, 198, 229)
    afternoon = Color(236, 174, 121)
    night = Color(0, 39, 89)
    sea = (64, 127, 204)
    sun = (248, 228, 143)
    moon = (229, 229, 229)
    cloud = (202, 204, 207)
    bg_color = day
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
        sun_x, sun_y = x, y

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
    else:
        bg_color = afternoon.lerp(night, (sun_y-250)/420)

    if sun_y < 550:
        draw.line(window, sun, (sun_x+50, sun_y-90), (sun_x+50, sun_y+90), 3) # top-bottom
        draw.line(window, sun, (sun_x-40, sun_y), (sun_x+140, sun_y), 3) # left-right
        draw.line(window, sun, (sun_x-5, sun_y-55), (sun_x+105, sun_y+55), 2) # top+left-bottom+right
        draw.line(window, sun, (sun_x-5, sun_y+55), (sun_x+105, sun_y-55), 2) # bottom+left-top+right
        draw.circle(window, sun, (sun_x+50, sun_y), 50) # circle
    else:
        draw.circle(window, moon, (sun_x+50, sun_y), 50)

    # Sea
    draw.rect(window, sea, (0, 500, 1280, 220))
    
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
    draw.rect(window, (187, 116, 86), (320, 260, 240, 240)) # house
    draw.rect(window, (160, 97, 54), (350, 356, 60, 96)) # window
    draw.rect(window, (160, 97, 54), (450, 340, 80, 160)) # door
    draw.polygon(window, (188, 66, 7), ((300, 260), (440, 140), (580, 260))) # top

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
                        if (10 <= x <= 310 and 510 <= y <= 710):
                            jogo = 'forca'
                            tema = ''
                        elif (330 <= x <= 630 and 510 <= y <= 710):
                            jogo = 'ppt'
                        elif (650 <= x <= 850 and 510 <= y <= 710):
                            jogo = 'calc'
                        elif (970 <= x <= 1270 and 510 <= y <= 710):
                            jogo = 'adiv'
                    case 'forca':
                        if palavra == '':
                            if (60 <= x <= 620 and 100 <= y <= 380):
                                tema = 'comida'
                                palavra = choice(palavras_comida)
                            elif (660 <= x <= 1220 and 100 <= y <= 380):
                                tema = 'jogos'
                                palavra = choice(palavras_jogos)
                            elif (60 <= x <= 620 and 420 <= y <= 700):
                                tema = 'pokemon'
                                palavra = choice(palavras_pokemon)
                            elif (660 <= x <= 1220 and 420 <= y <= 700):
                                tema = 'star wars'  
                                palavra = choice(palavras_starwars)
                            palavra_forca = '_' * len(palavra)
                            letras_tentadas = []
                    case 'ppt':
                        if jogada == 0:
                            if (60 <= x <= 420 and 60 <= y <= 660):
                                jogada = 1
                            elif (460 <= x <= 820 and 60 <= y <= 660):
                                jogada = 2
                            elif (860 <= x <= 1020 and 60 <= y <= 660):
                                jogada = 3
                            ppt_computador = randint(1, 3)
                            match (jogada, ppt_computador):
                                case (1, 1) | (2, 2) | (3, 3):
                                    texto = 'Empate!'
                                    print('entrou no match')
                                case (1, 2) | (2, 3) | (3, 1):
                                    texto = 'Você perdeu!'
                                    print('entrou no match')
                                    pontos -= 1
                                case (1, 3) | (2, 1) | (3, 2):
                                    texto = 'Você venceu!'
                                    print('entrou no match')
                                    pontos += 1
                    case 'adiv':
                        if adivinha == '':
                            if (60 <= x <= 620 and 100 <= y <= 700):
                                adivinha = 'jogador'
                                num_aleatorio = randint(min, max)
                                segunda_linha = 'Digite um número entre 1 e 1023'
                            elif (660 <= x <= 1220 and 100 <= y <= 700):
                                adivinha = 'computador'
                                num_chute = (min + max) // 2
                        elif adivinha == 'computador':
                            if (60 <= x <= 420 and 100 <= y <= 700):
                                max = num_chute
                                tentativas += 1
                            elif (460 <= x <= 820 and 100 <= y <= 700):
                                final = True
                            elif (860 <= x <= 1220 and 100 <= y <= 700):
                                min = num_chute
                                tentativas += 1
                            num_chute = (min + max) // 2
                    case 'calc':
                        final = False
                        # 0 -> 346 x 490, 574 y 718
                        if (346 <= x <= 490 and 574 <= y <= 718):
                            texto += '0'
                        # 1 -> 346 x 490, 428 y 572
                        elif (346 <= x <= 490 and 428 <= y <= 572):
                            texto += '1'
                        # 2 -> 494 x 638, 428 y 572
                        elif (494 <= x <= 638 and 428 <= y <= 572):
                            texto += '2'
                        # 3 -> 642 x 786, 428 y 572
                        elif (642 <= x <= 786 and 428 <= y <= 572):
                            texto += '3'
                        # 4 -> 346 x 490, 282 y 426
                        elif (346 <= x <= 490 and 282 <= y <= 426):
                            texto += '4'
                        # 5 -> 494 x 638, 282 y 426
                        elif (494 <= x <= 638 and 282 <= y <= 426):
                            texto += '5'
                        # 6 -> 642 x 786, 282 y 426
                        elif (642 <= x <= 786 and 282 <= y <= 426):
                            texto += '6'
                        # 7 -> 346 x 490, 136 y 280
                        elif (346 <= x <= 490 and 136 <= y <= 280):
                            texto += '7'
                        # 8 -> 494 x 638, 136 y 280
                        elif (494 <= x <= 638 and 136 <= y <= 280):
                            texto += '8'
                        # 9 -> 642 x 786, 136 y 280
                        elif (642 <= x <= 786 and 136 <= y <= 280):
                            texto += '9'
                        # + -> 790 x 934, 574 y 718
                        elif (790 <= x <= 934 and 574 <= y <= 718):
                            if opera == '':
                                if texto != '':
                                    num1 = float(texto)
                                else:
                                    num1 = resultado
                                    texto += str(num1)
                            else:
                                texto = texto[:-1]
                            texto += '+'
                            opera = '+'
                        # - -> 790 x 934, 428 y 572
                        elif (790 <= x <= 934 and 428 <= y <= 572):
                            if opera == ':':
                                if texto != '':
                                    num1 = float(texto)
                                else:
                                    num1 = resultado
                                    texto += str(num1)
                            else:
                                texto = texto[:-1]
                            texto += '-'
                            opera = '-'
                        # * -> 790 x 934, 282 y 426
                        elif (790 <= x <= 934 and 282 <= y <= 426):
                            if opera == '':
                                if texto != '':
                                    num1 = float(texto)
                                else:
                                    num1 = resultado
                                    texto += str(num1)
                            else:
                                texto = texto[:-1]
                            texto += '*'
                            opera = '*'
                        # / -> 790 x 934, 136 y 280
                        elif (790 <= x <= 934 and 136 <= y <= 280):
                            if opera == '':
                                if texto != '':
                                    num1 = float(texto)
                                else:
                                    num1 = resultado
                                    texto += str(num1)
                            else:
                                texto = texto[:-1]
                            texto += '/'
                            opera = '/'
                        # . -> 494 x 638, 574 y 718
                        elif (494 <= x <= 638 and 574 <= y <= 718):
                            texto += '.'
                        # = -> 642 x 786, 574 y 718
                        elif (642 <= x <= 786 and 574 <= y <= 718):
                            num2 = float(texto.partition(opera)[2])
                            if opera == '+':
                                resultado = num1 + num2
                            elif opera == '-':
                                resultado = num1 - num2
                            elif opera == '*':
                                resultado = num1 * num2
                            elif opera == '/':
                                resultado = num1 / num2
                            final = True
                            texto = ''
                            opera = ''
                        
                        # < -> 1038 x 1182 , 158 y 302
                        elif (1038 <= x <= 1182 and 158 <= y <= 302):
                            texto = texto[:-1]
                        # << -> 1038 x 1182 , 418 y 562
                        elif (1038 <= x <= 1182 and 418 <= y <= 562):
                            texto = ''

                        # sair -> 78 x 222, 288 y 432
                        elif (78 <= x <= 222 and 288 <= y <= 432):
                            texto = ''
                            resultado = 0
                            num1 = 0
                            num2 = 0
                            opera = ''
                            jogo = 'menu'


        if ev.type == KEYDOWN:
            if jogo == 'forca':
                if final == False:
                    pressionado = False
                    if K_a <= ev.key <= K_z:
                        chute += key.name(ev.key)
                    elif ev.key == K_BACKSPACE:
                        chute = chute[:-1]
                    elif ev.key == K_RETURN:
                        pressionado = True
                elif final == True:
                    if ev.key == K_BACKSPACE:
                        jogo = 'menu'
                        texto = ''
                    erros = 0
                    tema = ''
                    palavra = ''
                    final = False
                    pressionado = False
                    chute = ''
                    texto_extra = ''
                    texto = ''
            elif jogo == 'ppt':
                if ev.key == K_BACKSPACE:
                    jogo = 'menu'
                    pontos = 0
                    texto = ''
                jogada = 0
            elif jogo == 'adiv':
                if final == True:
                    if ev.key == K_BACKSPACE:
                        jogo = 'menu'
                        texto = ''
                    tentativas = 1
                    adivinha = ''
                    chute = ''
                    final = False
                    pressionado = False
                    segunda_linha = 'Digite um número entre 1 e 1023'
                    num_chute = 0
                    min = 1
                    max = 1023
                    texto_extra = ''
                else:
                    if ev.unicode.isdigit():
                        chute += ev.unicode
                        pressionado = False
                    elif ev.key == K_BACKSPACE:
                        chute = chute[:-1]
                        pressionado = False
                    elif ev.key == K_RETURN:
                        pressionado = True
                        num_chute = int(chute)
                        chute = ''
                        if num_chute == num_aleatorio:
                            final = True
            elif jogo == 'login':
                if inseriu_email == False:
                    if ev.key == K_BACKSPACE:
                        email = email[:-1]
                    elif ev.key == K_RETURN:
                            inseriu_email = True
                    else:
                        email += ev.unicode
                elif inseriu_senha == False:
                    if ev.key == K_BACKSPACE:
                        senha = senha[:-1]
                    elif ev.key == K_RETURN:
                            inseriu_senha = True
                            if valida_email(email) and valida_senha(senha):
                                jogo = 'menu'
                                texto = ''
                                cripto = codifica_cesar(senha)
                            else:
                                texto = 'Email ou senha inválido(s).'
                                inseriu_email = False
                                email = ''
                                inseriu_senha = False
                                senha = ''
                    else:
                        senha += ev.unicode
    

    window.fill(muito_claro)   

    match jogo:
        case 'forca':
            if tema == '':
                botoes('forca')
            else:
                match tema:
                    case 'comida':
                        write_text = fonte_menor.render('tema: comida!', True, medio_escuro)
                        window.blit(write_text, (480, 0))
                    case 'jogos':
                        write_text = fonte_menor.render('tema: jogos!', True, medio_escuro)
                        window.blit(write_text, (480, 0))
                    case 'pokemon':
                        write_text = fonte_menor.render('tema: pokémon!', True, medio_escuro)
                        window.blit(write_text, (480, 0))
                    case 'star wars':
                        write_text = fonte_menor.render('tema: star wars!', True, medio_escuro)
                        window.blit(write_text, (480, 0))

                desenhar_forca(erros)

                write_text = fonte_menor.render(palavra_forca, True, medio)
                window.blit(write_text, (350, 500))

                write_text = fonte_menor_ainda.render(chute, True, medio)
                window.blit(write_text, (350, 450))
                
                if pressionado:
                    if chute == palavra:
                        final = True
                        texto_extra = ''
                    else:
                        if len(chute) > 1:
                            pressionado = False
                            texto_extra = 'A palavra que você inseriu não está certa!'
                            chute = ''


                texto = 'Letras erradas: '
                segunda_linha = ', '.join(letras_tentadas)

                if pressionado:
                    texto_extra = ''
                    if final == False:
                        if erros < 6:
                            palavra_vazia = ''
                            if chute not in palavra:
                                if chute not in letras_tentadas:
                                    letras_tentadas.append(chute)
                                    erros += 1
                            for i in range(len(palavra)):
                                if chute == palavra[i]:
                                    palavra_vazia += chute
                                else:
                                    palavra_vazia += palavra_forca[i]
                            palavra_forca = palavra_vazia
                            if palavra_forca == palavra:
                                final = True
                        else:
                            final = True
                    else:
                        if erros == 6:
                            texto = 'Que pena, você perdeu! A palavra era:'
                            segunda_linha = palavra
                            texto_extra = mensagem_voltar
                        else:
                            texto = 'Parabéns! Você venceu! A palavra era:'
                            segunda_linha = palavra
                            texto_extra = mensagem_voltar
                            palavra_forca = palavra
                    chute = ''
                
                write_text = fonte_menor_ainda.render(texto, True, medio)
                window.blit(write_text, (370, 250))
                write_text = fonte_menor_ainda.render(segunda_linha, True, medio)
                window.blit(write_text, (370, 320))
                write_text = fonte_mini.render(texto_extra, True, medio)
                window.blit(write_text, (370, 390))
                
        case 'ppt':
            if jogada == 0:
                botoes('ppt')
            else:
                img_jogador = {1: pedra, 2: papel, 3: tesoura}.get(jogada)
                img_computador = {1: pedra, 2: papel, 3: tesoura}.get(ppt_computador)

                write_text = fonte.render(texto, True, medio_escuro)
                window.blit(write_text, (250, 0))
                write_text = fonte_menor_ainda.render('Sua jogada:', True, escuro)
                window.blit(write_text, (220, 150))
                window.blit(img_jogador, (190, 210))
                write_text = fonte_menor_ainda.render('Computador:', True, escuro)
                window.blit(write_text, (800, 150))
                window.blit(img_computador, (790, 210))

                write_text = fonte_mini.render(f'pontuação: {pontos}', True, medio)
                window.blit(write_text, (300, 600))
                write_text = fonte_mini.render(mensagem_voltar, True, medio)
                window.blit(write_text, (300, 650))

        case 'calc':
            botoes('calc')
            if final == False:
                text_surface = fonte_menor.render(texto, True, escuro)
                text_rect = text_surface.get_rect(midright=(930, 85))
                window.blit(text_surface, text_rect)
            else:
                text_surface = fonte_menor.render(str(resultado), True, escuro)
                text_rect = text_surface.get_rect(midright=(930, 85))
                window.blit(text_surface, text_rect)
        
        case 'adiv':
            if adivinha == '':
                botoes('adiv')
            elif adivinha == 'jogador':
                write_text = fonte_menor.render(chute, True, medio)
                window.blit(write_text, (350, 500))

                if pressionado:
                    if final:
                        texto = 'Parabéns, você venceu!'
                        segunda_linha = f'O número era {num_aleatorio}! Você acertou em {tentativas} tentativas'
                        window.blit(venceu, (490, 250))
                        texto_extra = mensagem_voltar
                    else:
                        segunda_linha = f'Número de chutes: {tentativas}'
                        if num_aleatorio < num_chute:
                            texto = f'O número é menor que {num_chute}'
                            tentativas += 1
                        else:
                            texto = f'O número é maior que {num_chute}'
                            tentativas += 1
                        pressionado = False

                    
                
                write_text = fonte_menor.render(texto, True, medio_escuro)
                window.blit(write_text, (200, 0))
                write_text = fonte_menor_ainda.render(segunda_linha, True, medio_escuro)
                window.blit(write_text, (100, 100))
                write_text = fonte_mini.render(texto_extra, True, medio)
                window.blit(write_text, (300, 600))
            elif adivinha == 'computador':
                if final == False:
                    botoes('adiv-comp')
                else:
                    write_text = fonte.render('O computador acertou!', True, medio_escuro)
                    window.blit(write_text, (40, 0))

                    write_text = fonte_menor.render(f'Número de chutes: {tentativas}', True, medio_escuro)
                    window.blit(write_text, (300, 100))
                    window.blit(venceu, (490, 250))

                    write_text = fonte_mini.render(mensagem_voltar, True, medio)
                    window.blit(write_text, (300, 600))

        case 'menu':
            casinha(x, y)
            botoes('menu')
        case 'login':
            botoes('login')

    display.update()