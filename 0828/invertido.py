# 3) Crie um programa em Python que leia um número inteiro entre 1000 e 9999
#    e escreva o número com os dígitos invertidos.
# Por exemplo:
# * 1412 => 2141
# * 2024 => 4202
# * 1000 => 1
# Nesta questão tu não podes utilizar strings.
# Deves utilizar operações matemáticas que vimos em aula, como o resto e divisão inteira.

numero = float(input("Digite um número inteiro entre 1000 e 9999: "))
while (numero < 1000 or numero > 9999) or (numero != int(numero)):
    numero = float(input("Digite um número inteiro entre 1000 e 9999: "))

numero = int(numero)

unidade = numero // 1000            # 1234              // 1000 = 1        = 1
dezena = numero % 1000 // 100 * 10  # 1234 % 1000 = 234 // 100  = 2 * 10   = 20
centena = numero % 100 // 10 * 100  # 1234 % 100  = 34  // 10   = 3 * 100  = 300
milhar = numero % 10 * 1000         # 1234 % 10   = 4           = 4 * 1000 = 4000

invertido = unidade + dezena + centena + milhar

print(invertido)
