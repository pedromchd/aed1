# 6)
# Faça um programa em python que leia 3 números e os mostre em ordem crescente.

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))

if n1 > n2:
    tmp = n1
    n1 = n2
    n2 = tmp

if n2 > n3:
    tmp = n2
    n2 = n3
    n3 = tmp

if n1 > n2:
    tmp = n1
    n1 = n2
    n2 = tmp

print(n1, n2, n3)
