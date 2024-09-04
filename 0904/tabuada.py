# Escrever a tabuada em um HTML

num = 1
print("<table border='1'><tr>")
print("<th>Numero</th><th>Fator</th><th>Produto</th></tr>")
while num <= 10:
    fator = 0
    while fator < 10:
        item = 0
        print(f"<tr><td>{num}</td><td>{fator}</td><td>{num * fator}</td></td>")
        fator = fator + 1
    num = num + 1
print("</tr></table>")
