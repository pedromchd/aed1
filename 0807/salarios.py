# 20)
# Escreva um programa que leia diversos funcionários e seu respectivo salario, ate que o nome de um funcionário seja “fim”.
# Em seguida escreva:
# a) O nome do funcionário com maior salário
# b) O nome do funcionário com menor salário
# c) A média dos salários digitados

func = input("Nome do funcionário: ")
sal = float(input(f"Salário de {func}: R$"))

max_sal = sal
max_fun = func

min_sal = sal
min_fun = func

media = sal
count = 1

while func != "fim":
    func = input("Nome do funcionário: ")
    if func != "fim":
        sal = float(input(f"Salário de {func}: R$"))
        if sal > max_sal:
            max_sal = sal
            max_fun = func
        if sal < min_sal:
            min_sal = sal
            max_fun = func
        media = media + sal
        count = count + 1

media = media / count

print(f"O funcionário com maior salário é {max_fun}")
print(f"O funcionário com menor salário é {min_fun}")
print(f"A média dos salários é {media:.2f}")
