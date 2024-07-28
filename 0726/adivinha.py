# Tentar adivinha o campeão

CAMPEAO = "morgana"
TENTATIVAS = 10

correto = False
tentativa = 1
while tentativa <= 7 and not correto:
    if tentativa == 2:
        print("Dica: É uma mulher")
    if tentativa == 3:
        print("Dica: É uma maga")
    if tentativa == 4:
        print("Dica: Pode ser jogada suporte, jungle ou mid")
    if tentativa == 5:
        print("Dica: É de Demácia")
    if tentativa == 6:
        print("Dica: Tem asas")
    if tentativa == 7:
        print("Dica: Tem uma irmã gêmea")
    campeao = input("Tente adivinhar o campeão de LOL: ")
    if campeao == CAMPEAO:
        correto = True
    else:
        print("Resposta incorreta, tente novamente.")
    tentativa = tentativa + 1

if correto:
    print("Parabéns por adivinhar!!")
else:
    print("Desculpe, a campeã correta era Morgana.")
