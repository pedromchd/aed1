# 18)
# Escreva um programa que calcule o fatorial de um número fornecido pelo usuário.
# O fatorial de um número n é o produto de todos os números inteiros de 1 a n.

n = int(input("Digite um número: "))

f = 1
while n > 0:
    f = f * n
    n = n - 1

print(f"O fatorial é: {f}")
