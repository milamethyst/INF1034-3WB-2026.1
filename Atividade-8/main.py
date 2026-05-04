def valida_email(email):
    return email[-8:] == '@puc.com'

def valida_senha(senha):
    return len(senha) >= 8 and tem_maiuscula(senha) and tem_minuscula(senha) and tem_numero(senha)

def tem_maiuscula(palavra):
    for letra in palavra:
        if letra.isupper():
            return True
    return False

def tem_minuscula(palavra):
    for letra in palavra:
        if letra.islower():
            return True
    return False

def tem_numero(palavra):
    for letra in palavra:
        if letra.isdigit():
            return True
    return False


# Você deverá escrever uma função booleana que irá determinar se uma senha é ou não boa (segura). 
# Foi definido que uma boa senha tem pelo menos 8 caracteres, que devem ser formados por pelo menos uma letra maiúscula, pelo menos uma letra minúscula e pelo menos um número. 
# Sua função deve retornar True se a senha passada para ela como seu único parâmetro é segura ou não. 
# Caso contrário, ela deve retornar False (100XP);