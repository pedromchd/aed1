# Calcular a raiz de um número natural

num = int(input("Digite um número: "))

while num < 0:
    num = int(input("Digite um número: "))

res = 0
raiz = 0
p = 1
while res != num:
    raiz = raiz + p
    res = raiz * raiz
    if res > num:
        if p < 1 / 10000:
            res = num
        raiz = raiz - p
        p = p / 10

print(f"{raiz:.4f}")
