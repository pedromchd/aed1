arq = open('poema.txt', 'r')

# arq -> ponteiro para o arquivo
# open -> abre o arquivo
# poema.txt -> nome do arquivo
# r -> modo: Read, Write, Append

print(arq)

texto = arq.read()

print(texto)

arq.close()
