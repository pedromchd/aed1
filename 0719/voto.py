# Leia o ano que nasceu e escreva se pode votar ou se é facultativo

from datetime import date

ANO_ATUAL = date.today().year

ano = int(input("Ano que nasceu: "))

idade = ANO_ATUAL - ano

if idade < 16:
    print("Não pode votar")

elif 18 <= idade <= 70:
    print("Voto obrigatório")

else:
    print("Voto facultativo")
