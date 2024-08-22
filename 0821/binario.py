# Converta um número decimal para binário.
# A conversão de números decimais em binários é realizada por meio da divisão sucessiva do número decimal por 2.
# Anotando-se o resto de cada divisão e invertendo a ordem deles para obter a representação binária do número.
# Por exemplo, para converter o número decimal 10 em binário, basta realizar as seguintes divisões:

"""
10 / 2 = 5 com resto 0

 5 / 2 = 2 com resto 1

 2 / 2 = 1 com resto 0

 1 / 2 = 0 com resto 1
"""

# Ao inverter a ordem dos restos, temos a representação binária do número 10 = 1010.

num = int(input("Digite um número: "))

bin = ""
while num != 0:
    bin = str(num % 2) + bin
    num = num // 2

print(bin)
