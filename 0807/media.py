# 19)
# Escreva um programa que leia diversos números até que o usuário digite zero.
# Em seguida escreva a média dos números digitados.

n = float(input("Digite um número: "))
m = n
c = 1
while n != 0:
    n = float(input("Digite um número: "))
    if n != 0:
        m = m + n
        c = c + 1

m = m / c

print(f"A média é: {m}")
