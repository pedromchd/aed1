# chr => converte um inteiro pra um caractere # chr(65) => "A"
# ord => converte um caractere para um nteiro # ord("a") => 97

cont = 0
while cont < 300:
    print(cont, chr(cont))
    cont = cont + 1

# Leia um nome e coloque todas as letras em minúsculo
# Considere que o usuário escreveu tudo em maíusculo
# Exemplo: "CAUA" --> "caua"

nome = input("Digite um nome: ")
indice = 0
nome_minusculo = ""
while indice < len(nome):
    letra = nome[indice]
    codigo = ord(letra)
    minusculo = codigo + 32
    # print(codigo, letra, minusculo, chr(minusculo))
    if 65 <= codigo <= 90:
        nome_minusculo = nome_minusculo + chr(minusculo)
    else:
        nome_minusculo = nome_minusculo + letra
    indice = indice + 1
print(nome_minusculo)
