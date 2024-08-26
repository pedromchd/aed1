# Receber um nome e separar nome por nome

nomes = input("Digite um nome: ")

i = 0
nome = ""
while i < len(nomes):
    char = nomes[i]
    if char == " ":
        if nome:
            print(nome)
        nome = ""
    else:
        nome = nome + char
    i = i + 1
if nome:
    print(nome)
