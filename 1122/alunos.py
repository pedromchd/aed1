# Leia o arquivo alunos.csv

# 1) Mostre todos os dados na tela
# 2) Liste apenas os nomes dos alunos
# 3) Mostre quem é o aluno mais novo

arq = open("1122/alunos.csv", "r", encoding="utf-8")

tudo = arq.readlines()

print(tudo)

for linha in tudo:
    print(linha[:-1])

for linha in tudo[1:]:
    print(linha.split(";")[1])

novo_nome = ""
novo_nasc = "0000-00-00"
for linha in tudo[1:]:
    nome = linha.split(";")[1]
    nascimento = linha.split(";")[2][:-1]
    if nascimento > novo_nasc:
        novo_nome = nome
        novo_nasc = nascimento
print(novo_nome)

arq.close()
