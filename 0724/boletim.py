# 4)
# Crie um programa em Python que leia as notas do estudante nos 4 bimestres da nossa disciplina e a frequência (em porcentagem).
# A seguir informe se o estudante passou por média, rodou ou ficou em exame.
# Para passar por média, o estudante deve ter média maior ou igual a 7.
# Estudante com média abaixo de 3 roda sem ao menos fazer o exame.
# O estudante que tiver menos de 75% de frequência também está rodado na disciplina.

n1 = float(input("Nota no bimestre 1: "))
n2 = float(input("Nota no bimestre 2: "))
n3 = float(input("Nota no bimestre 3: "))
n4 = float(input("Nota no bimestre 4: "))
fq = float(input("Frequência (%): "))

md = (n1 + n2 + n3 + n4) / 4

if md < 3 or fq < 75:
    print("Reprovado em AED1.")
else:
    if md < 7:
        print("Em exame em AED1.")
    else:
        print("Aprovado em AED1.")
