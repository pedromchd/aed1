# 2) Crie um programa em Python que leia uma data de 2024 ou de 2025 e escreva
#    qual o dia da semana corresponde à data.
# Observe que 2024 é um ano bissexto e que o ano começou em uma segunda-feira.
# Por exemplo:

# 12/01/2024 - segunda-feira
# 03/04/2024 - quarta-feira
# 31/03/2025 - segunda-feira
# 06/04/2025 - domingo

ano = int(input("Digite o ano: "))
while ano < 2024:
    print("Ano inválido.")
    ano = int(input("Digite o ano: "))

bissexto = False
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            bissexto = True
        else:
            bissexto = False
    else:
        bissexto = True

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
    while dia < 1 or (dia > 28 and not bissexto) or (dia > 29 and bissexto):
        print(f"Dia inválido para o mês {mes}.")
        dia = int(input("Digite o dia: "))

data = f"{dia}/{mes}/{ano}"

dia = 1
mes = 1
ano = 2024
temp = f"{dia}/{mes}/{ano}"

dias = 0

while temp != data:
    dia = dia + 1
    if dia > 28 and mes == 2 and not bissexto:
        mes = mes + 1
        dia = 1
    if dia > 29 and mes == 2 and bissexto:
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
    dias = dias + 1
    temp = f"{dia}/{mes}/{ano}"

print(data, end=" - ")

semana = (dias + ano - 2024) % 7

if semana == 0:
    print("segunda-feira")
if semana == 1:
    print("terça-feira")
if semana == 2:
    print("quarta-feira")
if semana == 3:
    print("quinta-feira")
if semana == 4:
    print("sexta-feira")
if semana == 5:
    print("sábado")
if semana == 6:
    print("domingo")
