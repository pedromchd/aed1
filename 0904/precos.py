# Pergunta por produtos para o usuário e os respectivos preços.
# Adiciona os items numa lista de compras até que o usuário digite ""
# Escreve os produtos da lista com seus preços.

compras = []
precos = []

produto = input("Digite o produto: ")

total = 0

while produto != "":
    preco = input(f"Digite o preço de {produto}: ")
    while preco == "":
        preco = input(f"Digite o preço de {produto}: ")
    compras.append(produto)
    precos.append(float(preco))
    total = total + float(preco)
    produto = input("Digite o produto: ")


item = 0
while item < len(compras):
    print(f"{compras[item]} -- R${precos[item]:.2f}")
    item = item + 1
print(f"total -- R${total:.2f}")

# item = 0
# print("<table border='1'><tr>")
# print("<th>Produto</th><th>Preço</th></tr>")
# while item < len(compras):
#     print(f"<tr><td>{compras[item]}</td><td>{precos[item]:.2f}</td></tr>")
# print("</tr></table>")
