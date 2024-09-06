# Leia uma senha e diga se ela é forte
# Tipos: Numérico, Alfabético e Especial
# Forte: 3 tipos
# Média: 2 tipos
# Fraca: 1 tipo

senha = input("Digite a senha: ")

numeros = "0123456789"
i = ord("A")
j = ord("a")
letras = ""
while i < ord("Z"):
    letras += chr(i) + chr(j)
    i += 1
    j += 1

tem_numero = False
tem_letra = False
tem_especial = False

forca = 0
tipos = ["Inválida", "Fraca", "Média", "Forte"]

for char in senha:
    if char in numeros:
        tem_numero = True
    else:
        if char in letras:
            tem_letra = True
        else:
            tem_especial = True

if tem_numero:
    forca += 1
if tem_letra:
    forca += 1
if tem_especial:
    forca += 1

print(tipos[forca])
