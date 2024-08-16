# 2) Leia um nome e:
# a) escreva apenas as vogais do nome;
# b) diga quantas vogais.

nome = input("Digite um nome: ")

v = 0
i = 0
while i < len(nome):
    if (
        nome[i] == "a"
        or nome[i] == "e"
        or nome[i] == "i"
        or nome[i] == "o"
        or nome[i] == "u"
    ):
        print(nome[i])
        v += 1
    i += 1

print(f"{v} vogais")

# Leia uma música e uma vogal alvo e escreva a musica trocando todas as vogais pela vogal alvo.

musica = input("Insira uma música: ")
vogal = input("Digite a vogal: ")

i = 0
misici = ""
while i < len(musica):
    letra = musica[i]
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        misici += vogal
    else:
        misici += letra
    i += 1

print(misici)
