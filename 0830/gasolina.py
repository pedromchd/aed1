# 1) Cada carro tem um desempenho, que é geralmente medido por quantos
#    quilômetros ele pode percorrer com 1 litro de gasolina.
# Por exemplo, os carros mais econômicos podem fazer 16 km/l.
# Escreva um programa em Python que leia o desempenho de um carro e um trajeto percorrido em um mês.
# Escreva o quanto foi gasto em reais, considerando a gasolina R$5,85.
# Por exemplo:

# Desempenho  | Trajeto  | Gasto
# ------------|----------|---------
# 12 km/l     | 1000 km  | R$ 487,50
# 16 km/l     | 1500 km  | R$ 548,44
# 8,9 km/l    | 2000 km  | R$ 1314,60

# Permita apenas valores positivos para desempenho e trajeto.

GASOLINA = 5.85

desempenho = float(input("Desempenho do carro (km/L): "))
trajeto = float(input("Trajeto percorrido em um mês (km): "))

litros = trajeto / desempenho

gasto = litros * GASOLINA

reais = int(gasto)
centavos = int(f"{gasto % reais * 100:.0f}")

print(f"R$ {reais},{centavos}")
