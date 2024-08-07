# 26)
# Construa um programa em Python que escreva uma contagem de 10 (dez) minutos, ou seja, mostre 0:00, e então 0:01, 0:02, ..., 0:58, 0:59, 1:00, 1:01,  ..., até 10:00.

seg = 0
while seg <= 600:
    min = seg // 60
    sec = seg % 60
    print(f"{min:02}:{sec:02}")
    seg = seg + 1
