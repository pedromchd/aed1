# 2) Crie um programa em Python que leia uma data inicial e um número de dias.
# Calcule e escreva a data correspondente ao número de dias.
# Por exemplo:
# * 01/01/2024 + 55 dias = 25/2/2024
# * 01/01/2024 + 150 dias = 31/5/2024
# * 01/01/2024 + 400 dias = 5/2/2025
# Não precisa considerar o ano bissexto, ou seja, pode considerar que todo fevereiro tem 28 dias.

ano = int(input("Digite o ano: "))
while ano < 0:
    print("Ano inválido.")
    ano = int(input("Digite o ano: "))

mes = int(input("Digite o mês: "))
while mes < 1 or mes > 12:
    print("Mês inválido.")
    mes = int(input("Digite o mês: "))

dia = int(input("Digite o dia: "))
while dia < 1 or dia > 31:
    print(f"Dia inválido para o mês {mes}.")
    dia = int(input("Digite o dia: "))
if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    while dia < 1 or dia > 30:
        print(f"Dia inválido para o mês {mes}.")
        dia = int(input("Digite o dia: "))
if mes == 2:
    while dia < 1 or dia > 28:
        print(f"Dia inválido para o mês {mes}.")
        dia = int(input("Digite o dia: "))

print(f"Data inicial: {dia}/{mes}/{ano}")

dias = int(input("Digite um número de dias: "))
while dias < 0:
    dias = int(input("Digite um número de dias: "))

while dias > 0:
    dia = dia + 1
    if dia > 28 and mes == 2:
        mes = mes + 1
        dia = 1
    if dia > 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        mes = mes + 1
        dia = 1
    if dia > 31:
        mes = mes + 1
        dia = 1
    if mes > 12:
        ano = ano + 1
        mes = 1
    dias = dias - 1

print(f"Data final: {dia}/{mes}/{ano}")
