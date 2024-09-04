# 3) Crie um programa em Python que leia um número inteiro e escreva
#    a soma dos números correspondentes a cada dígito do número.
# Por exemplo:

# Número    | Soma
# ----------|---------
# 1412      | 8
# 4341220   | 16
# 101       | 2

# Nesta questão tu não podes utilizar strings.
# Deves utilizar operações matemáticas que vimos em aula, como o resto e divisão inteira.

num = float(input("Digite um número: "))
while num != int(num):
    print("O número deve ser inteiro.")
    num = float(input("Digite um número: "))
num = int(num)

soma = 0
while num > 0:
    soma = soma + num % 10
    num = num // 10

print(soma)
