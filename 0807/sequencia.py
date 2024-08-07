# 25)
# Considere uma sequência de números que atende a todos critérios abaixo:
# a) Possui sempre 2 dígitos, nem mais, nem menos.
# b) A representação do número possui pelo menos um dígito 1 ou um dígito 2.
# c) O número é múltiplo de 3.
# Faça um programa que implemente e mostre essa sequência.
# obs: tem que usar repetição para mostrar a sequência.
# Não pode mostrar os números “na mão”.

n = 10
while n < 100:
    if not n % 3:
        stmt1 = n % 10 == 1 or n % 10 == 2
        stmt2 = n // 10 == 1 or n // 10 == 2
        if stmt1 or stmt2:
            print(n, end=" ")
    n = n + 1
