# 1)
# Faça um programa que, ao receber os valores da largura e do comprimento de uma figura geométrica, mostre se esta é um quadrado ou apenas um retângulo.
# Caso um valor seja menor ou igual a zero, deve-se mostrar um erro.

largura = float(input("Largura da figura: "))
comprim = float(input("Comprimento da figura: "))

if largura > 0 and comprim > 0:
    if largura == comprim:
        print("É um quadrado.")
    else:
        print("É apenas um retângulo.")
else:
    print("Erro: valores inválidos para forma geométrica.")
