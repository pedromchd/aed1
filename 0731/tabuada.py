# 13)
# Escreva um programa que mostre a tabuada (0 a 10) de um número fornecido pelo usuário.

numero = float(input("Insira um número: "))

cont = 0
while cont <= 10:
    tabuada = numero * cont
    print(f"{numero} x {cont} = {tabuada}")
    cont = cont + 1
