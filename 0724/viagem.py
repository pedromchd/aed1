# 2)
# Faça um programa em python que pergunte ao usuário o seguinte:
#   A viagem custará menos de R$ 30?
#   Terá Wifi?
#   Terá piscina?
#   Terá churrasqueira?
# O programa deverá mostrar se a viagem ocorrerá de acordo com as seguintes regras:
#   Deverá custar menos de R$ 30
#   Tem que ter wifi e piscina
#   Se não tiver wifi ou piscina, tem que ter churrasqueira

menos30 = input("A viagem custará menos de R$30? (sim/nao) ") == "sim"  # M
wifi = input("A viagem terá wifi? (sim/nao) ") == "sim"  # W
piscina = input("A viagem terá piscina? (sim/nao) ") == "sim"  # P
churras = input("A viagem terá churrasqueira? (sim/nao) ") == "sim"  # C

# se nao W ou nao P ent C => se nao (W e P) ent C
# nao nao (W e P) ou C => W e P ou C

if menos30 and (wifi and piscina or churras):
    print("A viagem ocorrerá!")
else:
    print("A viagem não ocorrerá... :(")
