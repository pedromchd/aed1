import random

random.seed()
sorte = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
while i < 100:
    valor = random.randint(0, 10)
    sorte[valor] += 1
    print(sorte)
    i += 1
