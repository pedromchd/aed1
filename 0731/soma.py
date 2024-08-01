# 15)
# Escreva um programa que calcule e mostre a soma dos números de 1 a N.
# Não utilize as equações de progressão aritmética.

num = int(input("Somar números de 1 até "))

sum = 0
con = 0
while num >= 0:
    sum = sum + con
    con = con + 1
    num = num - 1

print(sum)
