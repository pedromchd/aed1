def tabuada(num):
    saida = ""
    for i in range(11):
        mult = num * i
        saida += f"{num} * {i} = {mult}\n"
    return saida


nums = int(input("numeros "))

for i in range(1, nums + 1):
    print(tabuada(i))
