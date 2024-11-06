# Converter um número decimal para binário


def binario(num: int) -> str:
    if num == 0:
        return "0"

    bin = ""
    while num > 0:
        bin = f"{num % 2}{bin}"
        num //= 2
    return bin


num = int(input("digite um número decimal: "))

print(binario(num))
