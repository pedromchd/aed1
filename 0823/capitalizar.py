# Ler um nome e capitalizar ele
# Considere que o usuário escreveu tudo em minúsculo
# Exemplo: "pedro machado" => "Pedro Machado"
# Exemplo: "alex dos santos" => "Alex dos Santos"

nome = input("Digite um nome: ")

capitalizado = ""

parcial = ""

i = 0
while i <= len(nome):
    if i == len(nome):
        letra = " "
    else:
        letra = nome[i]
    if letra == " ":
        if len(parcial) > 3:
            primeira = parcial[0]
            minuscula = ord(primeira)
            capital = chr(minuscula - 32)
            j = 1
            while j < len(parcial):
                capital = capital + parcial[j]
                j = j + 1
            capitalizado = capitalizado + capital + letra
        else:
            capitalizado = capitalizado + parcial + letra
        parcial = ""
    else:
        parcial = parcial + letra
    i = i + 1

print(capitalizado)
