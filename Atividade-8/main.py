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
        if caracter.isdigit():
            ref = ord('0')
            decimal = ord(caracter) # transforma na posição na tabela ascii
            decimal -= ref # subtrai o valor de referência
            decimal += 3 # adiciona 3
            decimal = decimal % (ord('9') - ref + 1) # obtem o resto (do máximo menos a referência + 1)
            decimal += ref # soma o valor de referência
            senha_nova += chr(decimal) # adiciona o caracter novo na senha criptografada
        elif caracter.islower():
            ref = ord('a')
            decimal = ord(caracter)
            decimal -= ref
            decimal += 3
            decimal = decimal % (ord('z') - ref + 1)
            decimal += ref
            senha_nova += chr(decimal)
        elif caracter.isupper():
            ref = ord('A')
            decimal = ord(caracter)
            decimal -= ref
            decimal += 3
            decimal = decimal % (ord('Z') - ref + 1)
            decimal += ref
            senha_nova += chr(decimal)
        else:
            senha_nova += caracter
    return senha_nova


print(codifica_cesar('Abc@123Zz'))