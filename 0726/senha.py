SENHA = "PEPEPE"
TENTATIVAS = 5

acesso = False
tentativa = 1

while not acesso and tentativa <= TENTATIVAS:
    senha = input("Para acessar, digite a senha: ")
    if senha == SENHA:
        acesso = True
    else:
        print(f"Senha incorreta.\nTentativa {tentativa}. ", end="")
        tentativa = tentativa + 1

if acesso:
    print("Bem-vindo ao sistema!")
else:
    print("Acesso negado.")
