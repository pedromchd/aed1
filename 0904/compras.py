# Pergunta por produtos para o usuário.
# Adiciona os items numa lista de compras até que o usuário digite ""
# Escreve os produtos da lista.

compras = []

produto = input("Digite o produto: ")

while produto != "":
    compras.append(produto)
    produto = input("Digite o produto: ")


for produto in compras:
    print(produto)
