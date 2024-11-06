# Converter um número binário para decimal


def decimal(bin: str) -> int:
    num = 0

    i = 0
    while i < len(bin):
        bit = bin[-(i + 1)]

        num += 2**i * int(bit)

        i += 1

    return num


bin = input("digite um número binário: ")

print(decimal(bin))
