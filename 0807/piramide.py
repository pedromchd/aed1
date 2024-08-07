# 27)
# Faça um programa em python que desenhe uma pirâmide conforme 2 dados informados pelo usuário.
# O primeiro dado indica o "tijolo" e o segundo a quantidade de andares.
# Ex: Informe o tijolo: A
#     Informe a quantidade de andares: 5
#     A
#    AAA
#   AAAAA
#  AAAAAAA
# AAAAAAAAA

tijolo = input("Tijolo: ")
altura = int(input("Número de andares: "))

cont = 1
while cont <= altura:
    andar = altura - cont
    print(" " * andar + tijolo * (2 * cont - 1))
    cont = cont + 1
