# Leia os lados de um triângulo e escreva se é válido e o tipo (equilátero, isósceles e escaleno)

TIPOS = ["Escaleno", "Isósceles", "Equilátero"]
tipo = 0

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

if a + b > c and a + c > b and b + c > a:
    if a == b:
        tipo += 1
    if b == c:
        tipo += 1
    print(f"Triângulo {TIPOS[tipo]}")
else:
    print("Não é um triângulo válido")
