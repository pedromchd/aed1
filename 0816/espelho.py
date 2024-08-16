# 3) Leia uma palavra e mostre seu espelho:
# - andre -> erdna
# - casa -> asac
# - ana -> ana

palavra = input("Digite uma palavra: ")
espelho = ""

i = 1
while i <= len(palavra):
    espelho += palavra[-i]
    i += 1

print(espelho)


# b) Leia um nome e faça o espelho do nome.

nome = input("Digite um nome: ")
emon = ""

i = 1
mirr = ""
while i <= len(nome):
    letra = nome[-i]
    if letra == " ":
        emon = letra + mirr + emon
        mirr = ""
        i += 1
    mirr += nome[-i]
    i += 1
emon = mirr + emon

print(emon)
