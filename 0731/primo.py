# 16)
# Escreva um programa que receba um número inteiro positivo do usuário e verifique se ele é primo.

num = int(input("Digite um número: "))

con = 1
res = "É primo"
while con <= num:
    if num == 1:
        res = "Não é primo"
    if not num % con and 1 < con < num:
        res = "Não é primo"
    con = con + 1

print(res)
