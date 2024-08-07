# 23)
# Escreva um programa que leia dois valores x e y.
# Em seguida escreva quais são os números primos contidos neste intervalo.
# Por exemplo, para x=3 e y=14 escreva: 3,5,7,11,13. Verifique se o usuário digitou x e y de modo que x<y.

x = int(input("Início: "))
y = int(input("Fim: "))
while y < x:
    y = int(input("Fim: "))

while x < y:
    c = 1
    p = True
    while c <= x:
        if x == 1:
            p = False
        if not x % c and 1 < c < x:
            p = False
        c = c + 1
    if p:
        print(x, end=", ")
    x = x + 1
