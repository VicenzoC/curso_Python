lista = list()
dados = list()
abaixo = acima = 0
nacima = list()
nabaixo = list()
while True:
    n = str(input('Nome ("EXIT" para sair): '))
    if n == "EXIT":
        break
    p = float(input('Peso: '))
    dados.append(n)
    dados.append(p)
    if len(lista) == 0:
        abaixo = acima = p
    else:
        if p > acima:
            acima = p
        if p < abaixo:
            abaixo = p
    lista.append(dados[:])
    dados.clear()
qtd = len(lista)
for p in lista:
    if p[1] == acima:
        nacima.append(p[0])
    if p[1] == abaixo:
        nabaixo.append(p[0])
print(f'A) A quantidade de pessoas que foram cadastradas foi: {qtd}\n'
      f'B) O maior peso foi de {acima} {nacima}\n'
      f'C) O menor peso foi de {abaixo} {nabaixo}')
