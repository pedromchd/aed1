# 24)
# Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
# A melhor e a pior nota são eliminadas.
# A sua nota fica sendo a média dos votos restantes.
# Faça um programa em Python que receba o nome do(a) ginasta, e as notas de sua apresentação dadas pelos sete jurados.
# Ao final, informe a melhor nota, a pior nota e a sua média final, conforme a descrição acima informada (ou seja, retirar a melhor e a pior nota para calcular a média).
# As notas não são informadas em ordem (crescente ou decrescente).

ginasta = input("Nome da ginasta: ")

nota = float(input(f"Nota do jurado 1: "))

max_nota = nota
min_nota = nota

media = nota

count = 2
while count <= 7:
    nota = float(input(f"Nota do jurado {count}: "))
    if nota > max_nota:
        max_nota = nota
    if nota < min_nota:
        min_nota = nota
    media = media + nota
    count = count + 1

media = media - min_nota - max_nota
media = media / 5

print(f"A melhor nota foi {max_nota}")
print(f"A pior nota foi {min_nota}")
print(f"A média final foi {media}")
