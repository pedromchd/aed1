# 3)
# Construa um programa em python que, informadas três medidas a, b e c pelo usuário, verifique se elas podem ser lados de um triângulo.
# Se não puderem ser, primeiramente o algoritmo deve informar isso.
# Se for possível serem lados de triângulo, deve dizer qual tipo de triângulo pode ser construído com essas medidas (isósceles, escaleno ou equilátero).
# A condição para formar um triângulo: comprimento do maior segmento seja inferior à soma dos comprimentos dos dois menores.

tipo = 1

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

if a + b > c and a + c > b and b + c > a:
    if a == b:
        tipo += 1
    if b == c:
        tipo += 1
else:
    print("Não é um triângulo válido")
    tipo = 0

if tipo == 1:
    print("Triângulo escaleno")
if tipo == 2:
    print("Triângulo isósceles")
if tipo == 3:
    print("Triângulo equilátero")
