# Ler um nome e capilazá-lo

nome = "pEDRO GaRcIa MACHado"

print(nome)

nome = nome.lower()

print(nome)

lista = nome.split(" ")

# print(lista)

capital = ""

prepos = ["e", "de", "da", "do", "das", "dos"]

for nome in lista:
    if nome in prepos:
        capital += nome
    else:
        capital += nome[0].upper()
        i = 1
        while i < len(nome):
            capital += nome[i]
            i += 1
    capital += " "

# for nome in lista:
#     capital += nome[0].upper()
#     i = 1
#     while i < len(nome):
#         capital += nome[i].lower()
#         i += 1
#     capital += " "

# for nome in lista:
#     codigo = ord(nome[0])
#     if ord("a") <= codigo <= ord("z"):
#         capital += chr(codigo - 32)
#     else:
#         capital += nome[0]

#     i = 1
#     while i < len(nome):
#         codigo = ord(nome[i])
#         if ord("A") <= codigo <= ord("Z"):
#             capital += chr(codigo + 32)
#         else:
#             capital += nome[i]
#         i += 1
#     capital += " "

print(capital)
