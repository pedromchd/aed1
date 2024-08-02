# Monte uma pirâmide dada altura
#       1
#     2 2 2
#   3 3 3 3 3
# 4 4 4 4 4 4 4

altura = int(input("Altura: "))
tijolo = input("Tijolo: ")

andar = 1
cont = 1

espaco = " "
desloc = altura - 1

# while andar <= altura:
#     print(desloc * espaco + cont * tijolo)
#     andar = andar + 1
#     cont = cont + 2
#     desloc = desloc - 1

# Concatenando string

while andar <= altura:
    cont2 = 0
    espaco_montado = ""
    while cont2 < desloc:
        espaco_montado = espaco_montado + espaco
        cont2 = cont2 + 1
    cont2 = 0
    tijolo_montado = ''
    while cont2 < cont:
        tijolo_montado = tijolo_montado + tijolo
        cont2 = cont2 + 1
    print(espaco_montado + tijolo_montado)
    andar = andar + 1
    cont = cont + 2
    desloc = desloc - 1
