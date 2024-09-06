# Leita uma string e verifique se é palíndromo

palavra = input("Digite uma palavra: ").lower()

i = 1
arvalap = ""
while i <= len(palavra):
    arvalap += palavra[-i]
    i += 1

if palavra == arvalap:
    print("É palíndromo.")
else:
    print("Não é palíndromo.")
