# 22)
# Faça um programa em python que leia um valor inteiro X.
# Em seguida apresente os 6 valores ímpares consecutivos a partir de X, inclusive o X se for o caso.
# Por exemplo, para o número 8, a saída será “9,11,13,15,17,19”.

n = int(input("Digite um número: "))

c = 0
while c < 6:
    i = n + 1 - (n % 2) + c * 2
    print(i, end=", ")
    c = c + 1
