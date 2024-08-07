# 17)
# Escreva um programa que mostre a sequência de Fibonacci até o enésimo termo (n deve ser informado pelo usuário).
# A sequência de Fibonacci é aquela em que cada termo é a soma dos dois termos anteriores.
# Por exemplo, para n=8 escreva 0, 1, 1, 2, 3, 5, 8 e 13.

n = int(input("Mostrar quantos números? "))

i = 0
fibo = 0
prox = 1
while i < n:
    print(fibo, end=", ")
    soma = fibo + prox
    fibo = prox
    prox = soma
    i = i + 1
