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

def casinha(x, y):
    global cloud_x, cloud_direction
    day = Color(16, 198, 229)
    afternoon = Color(236, 174, 121)
    night = Color(0, 39, 89)
    sea = (64, 127, 204)
    sun = (248, 228, 143)
    moon = (229, 229, 229)
    cloud = (202, 204, 207)
    sun_x = 500
    sun_y = 100
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
