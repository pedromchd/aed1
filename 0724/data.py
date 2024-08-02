# 7)
# Crie um programa em Pyhon que leia uma data (DD/MM/AAAA) e diga se a data é válida.
# a) Desconsidere anos bissextos.

res = "Data inválida."

dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano: "))

if ano >= 0:
    if 1 <= mes <= 12:
        if 1 <= dia:
            if (
                mes == 1
                or mes == 3
                or mes == 5
                or mes == 7
                or mes == 8
                or mes == 10
                or mes == 12
            ) and dia <= 31:
                res = "Data válida!"
            if (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia <= 30:
                res = "Data válida!"
            if mes == 2 and dia <= 28:
                res = "Data válida!"

# b) Considere anos bissextos

if ano >= 0:
    if 1 <= mes <= 12:
        if 1 <= dia:
            if (
                mes == 1
                or mes == 3
                or mes == 5
                or mes == 7
                or mes == 8
                or mes == 10
                or mes == 12
            ) and dia <= 31:
                res = "Data válida!"
            if (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia <= 30:
                res = "Data válida!"
            if mes == 2 and dia <= 28 and ano % 4:
                res = "Data válida!"
            if mes == 2 and dia <= 29 and not (ano % 4):
                res = "Data válida!"

print(res)
