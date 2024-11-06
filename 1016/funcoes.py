def dobro(num):
    saida = num * 2
    return saida

def eh_par(valor):
    if valor % 2 == 0:
        return True
    return False

def teste():
    print("Volta as aulas")
    return 2
    print("Amamos grama sendo cortada")

numero = int(input("Digite o número: "))
duplo = dobro(numero)
print(duplo + 1)

if eh_par(duplo):
    print("É par")
else:
    print("É ímpar")
