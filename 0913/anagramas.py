# 1.a. Leia duas palavras e escreva se elas são anagramas

str1 = input("digite: ")
str2 = input("digite: ")

print(str1, str2)

cont1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# cont2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

if len(str1) == len(str2):
    print("pode ser anagrama....")
    for letra in str1:
        i = ord(letra) - ord("a")
        cont1[i] += 1

    for letra in str2:
        i = ord(letra) - ord("a")
        cont1[i] -= 1
        # cont2[i] += 1

    anagrama = True
    i = 0
    while anagrama and i < len(cont1):
        if cont1[i] != 0:  # cont2[i]:
            anagrama = False
        i += 1

    if anagrama:
        print("É um anagrama!")
    else:
        print("Não é anagrama....")

print(cont1)
# print(cont2)
