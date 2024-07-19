# Peça para o usuário informar seu nome e a hora do dia
# Escreva uma mensagem conforme a hora

nome = input("Qual seu nome? ")
hora = int(input("Qual a hora do dia? "))

saudacao = "Boa noite"

if hora < 18:
    saudacao = "Boa tarde"
    if hora < 12:
        saudacao = "Bom dia"

print (saudacao, nome)
