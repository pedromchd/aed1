# Leia um número e mostre sua tabuada

TABUADA = 10

numero = float(input("Insira um número: "))

cont = 0
while cont <= TABUADA:
    tabuada = numero * cont
    print(f"{numero} x {cont} = {tabuada}")
    cont = cont + 1
