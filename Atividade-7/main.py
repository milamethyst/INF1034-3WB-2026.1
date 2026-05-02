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

pedra = image.load("./Atividade-7/Recursos/Botões/Pedra Papel Tesoura/pedra.png")
pedra = transform.scale(pedra, (300, 300))
papel = image.load("./Atividade-7/Recursos/Botões/Pedra Papel Tesoura/papel.png")
papel = transform.scale(papel, (300, 300))
tesoura = image.load("./Atividade-7/Recursos/Botões/Pedra Papel Tesoura/tesoura.png")
tesoura = transform.scale(tesoura, (300, 300))

fonte = font.Font("./Atividade-7/Recursos/Outros/font.otf", 120)
fonte_menor = font.Font("./Atividade-7/Recursos/Outros/font.otf", 80)
fonte_menor_ainda = font.Font("./Atividade-7/Recursos/Outros/font.otf", 60)
fonte_mini = font.Font("./Atividade-7/Recursos/Outros/font.otf", 30)


# variáveis
mensagem_voltar = 'pressione enter para jogar de novo ou backspace para voltar'
jogo = 'menu'
erros = 0
tema = ''
palavra = ''
palavra_forca = ''
letras_tentadas = []
final = False
pressionado = False
texto = ''
chute = ''
texto_extra = ''
jogada = 0

# listas palavras
palavras_comida = ['arroz', 'banana', 'queijo', 'alface', 'frango', 'amendoim', 'chocolate', 'pepino', 'batata', 'couve', 'carne']
palavras_jogos = ['controle', 'steam', 'playstation', 'xbox', 'nintendo', 'overwatch', 'valorant', 'console', 'minecraft', 'computador', 'mouse', 'teclado', 'ranqueada', 'genshin', 'atari', 'gameboy', 'overcooked', 'fortnite', 'undertale', 'deltarune', 'bloons', 'megabonk', 'peak', 'spiritfarer']
palavras_pokemon = ['pikachu', 'wooper', 'quagsire', 'oshawott', 'piplup', 'lucario', 'bulbasaur', 'ivysaur', 'venusaur', 'charmander', 'charmeleon', 'charizard', 'squirtle', 'wartortle', 'blastoise', 'caterpie', 'metapod', 'butterfree', 'weedle', 'kakuna', 'beedrill', 'pidgey', 'pidgeotto', 'pidgeot', 'rattata', 'raichu', 'vaporeon', 'jolteon', 'flareon', 'espeon', 'umbreon', 'leafeon', 'glaceon', 'sylveon', 'eevee', 'clefairy', 'clefable', 'vulpix', 'ninetales', 'zubat', 'jigglypuff', 'meowth', 'psyduck', 'growlithe', 'arcanine', 'poliwag', 'poliwhirl', 'abra', 'machop', 'weepinbell', 'geodude', 'ponyta', 'slowpoke', 'gengar', 'chansey', 'horsea', 'magikarp', 'gyarados', 'ditto', 'lapras', 'snorlax', 'dragonite', 'chikorita', 'cyndaquil', 'typhlosion', 'totodile', 'togepi', 'mareep']
palavras_starwars = ['skywalker', 'vader', 'jedi', 'anakin', 'sith', 'yoga']

# funções
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

def pedra_papel_tesoura(jogada):
    ppt_computador = randint(1, 3)
    match (jogada, ppt_computador):
        case (1, 1):
            img_jogador = pedra
            img_computador = pedra
            texto = 'Empate!'
        case (1, 2):
            img_jogador = pedra
            img_computador = papel
            texto = 'Você perdeu!'
        case (1, 3):
            img_jogador = pedra
            img_computador = tesoura
            texto = 'Você venceu!'
        case (2, 1):
            img_jogador = papel
            img_computador = pedra
            texto = 'Você venceu!'
        case (2, 2):
            img_jogador = papel
            img_computador = papel
            texto = 'Empate!'
        case (2, 3):
            img_jogador = papel
            img_computador = tesoura
            texto = 'Você perdeu!'
        case (3, 1):
            img_jogador = tesoura
            img_computador = pedra
            texto = 'Você perdeu!'
        case (3, 2):
            img_jogador = tesoura
            img_computador = papel
            texto = 'Você venceu!'
        case (3, 3):
            img_jogador = tesoura
            img_computador = tesoura
            texto = 'Empate!'
        
    return img_jogador, img_computador, texto

def botoes(modo):
    if modo == 'menu':
        write_text = fonte.render('jogos!', True, medio_escuro)
        window.blit(write_text, (520, 0))
        draw.rect(window, botao, (60, 100, 560, 280), 0, 20)
        window.blit(forca, (240, 140))
        draw.rect(window, botao, (660, 100, 560, 280), 0, 20)
        window.blit(ppt, (840, 140))
        draw.rect(window, botao, (60, 420, 560, 280), 0, 20)
        window.blit(calculadora, (240, 460))
        draw.rect(window, botao, (660, 420, 560, 280), 0, 20)
        window.blit(adivinhacao, (840, 460))

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



while running:
    clock.tick(60)
    x, y = mouse.get_pos()
    keys = key.get_pressed()

    for ev in event.get():
        if ev.type == QUIT:
            running = False
        if ev.type == MOUSEBUTTONDOWN:
            if ev.button == 1:
                match jogo:
                    case 'menu':
                        if (60 <= x <= 620 and 100 <= y <= 380):
                            jogo = 'forca'
                            tema = ''
                        elif (660 <= x <= 1220 and 100 <= y <= 380):
                            jogo = 'ppt'
                        elif (60 <= x <= 620 and 420 <= y <= 700):
                            jogo = 'calc'
                        elif (660 <= x <= 1220 and 420 <= y <= 700):
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
                                img_jogador, img_computador, texto = pedra_papel_tesoura(jogada)
                            elif (460 <= x <= 820 and 60 <= y <= 660):
                                jogada = 2
                                img_jogador, img_computador, texto = pedra_papel_tesoura(jogada)
                            elif (860 <= x <= 1020 and 60 <= y <= 660):
                                jogada = 3
                                img_jogador, img_computador, texto = pedra_papel_tesoura(jogada)

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
                    erros = 0
                    tema = ''
                    palavra = ''
                    final = False
                    pressionado = False
                    chute = ''
                    texto_extra = ''
            elif jogo == 'ppt':
                if ev.key == K_BACKSPACE:
                    jogo = 'menu'
                jogada = 0

    

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
                write_text = fonte_menor_ainda.render('Sua jogada:', True, escuro)
                window.blit(write_text, (220, 150))
                window.blit(img_jogador, (190, 210))
                write_text = fonte_menor_ainda.render('Computador:', True, escuro)
                window.blit(write_text, (800, 150))
                window.blit(img_computador, (790, 210))
                write_text = fonte.render(texto, True, medio_escuro)
                window.blit(write_text, (420, 0))

                write_text = fonte_mini.render(mensagem_voltar, True, medio)
                window.blit(write_text, (300, 600))

        case 'calc':
            botoes('calc')
        case 'adiv':
            botoes('adiv')
        case default:
            botoes('menu')

    display.update()