# 1) Crie um programa que leia os dois lados de um retângulo e escreva a sua área.
# Verifique para que o usuário digite apenas números positivos para representar os lados.

a = float(input("Digite o lado A do retângulo: "))
while a < 1:
    print("O lado A deve ser um número positivo.")
    a = float(input("Digite o lado A do retângulo: "))

b = float(input("Digite o lado B do retângulo: "))
while b < 1:
    print("O lado B deve ser um número positivo.")
    b = float(input("Digite o lado B do retângulo: "))

area = a * b

print(f"A área do retângulo é {area}")
