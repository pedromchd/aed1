# 4) Crie um programa em Python que leia um número inteiro e escreva
#    todos os divisores desse número.
# Por exemplo:

# Número    | Divisores
# ----------|---------
# 14        | 1,2,7,14
# 17        | 1,17
# 24        | 1,2,3,4,6,8,12,24

num = float(input("Digite um número: "))
while num != int(num):
    print("O número deve ser inteiro.")
    num = float(input("Digite um número: "))
num = int(num)

i = 2
div = "1"
while i <= num:
    if not num % i:
        div = f"{div},{i}"
    i = i + 1

print(div)
