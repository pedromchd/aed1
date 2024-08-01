# Monte uma pirâmide dada altura
#       1
#     2 2 2
#   3 3 3 3 3
# 4 4 4 4 4 4 4

h = int(input("Altura da pirâmide: "))

i = 1
while i <= h:
    e = 2 * h - 2 * i
    w = 2 * i - 1
    i = i + 1
    print(" " * e + "# " * w)
