# Fazer a tabuada de N números

n = int(input("Quantas tabuadas? "))

i = 1
while i <= n:
    j = 0
    print(f"TABUADA DO {i}")
    while j <= 10:
        print(f"{i} * {j} = {i * j}")
        j = j + 1
    i = i + 1
    print()
