# 21)
# Escreva um programa de adivinhação de número.
# O programa deve conter um número secreto entre 1 e 1.000.000.
# O usuário deve chutar um número e o programa deve dizer se o número chutado é maior ou menor que o número secreto.
# O usuário deve tentar até acertar o número secreto.
# O código abaixo mostrar como sortear um número aleatório entre 0 e 10 em python:

import random

sorteado = random.randint(0, 1_000_000)

num = int(input("Chute um número: "))

while num != sorteado:
    print("Errrouuu!", end=" ")
    if num < sorteado:
        print("O número chutado é menor que o sorteado")
    if num > sorteado:
        print("O número chutado é maior que o sorteado")
    num = int(input("Chute um número: "))

print("Parabéns! Você adivinhou o número!")
