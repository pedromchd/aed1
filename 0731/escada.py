# 14)
# Escreva um programa que mostre a seguinte sequência de números para um valor N informado pelo usuário:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# …
# N N N N N N N …

N = int(input("Digite o número de degraus: "))

cont = 1
while cont <= N:
    print(f"{cont} " * cont)
    cont = cont + 1
