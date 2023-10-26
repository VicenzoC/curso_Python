cont = pmax = pmin = soma = cont1000 = 0
nmax = nmin = ''
while True:
    nome = str(input('Qual o nome do produto? ')).strip()
    valor = float(input('Qual o preço do produto? R$'))
    if cont == 0:
        pmax = pmin = valor
        nmax = nmin = nome
    else:
        if valor > pmax:
            pmax = valor
            nmax = nome
        if valor < pmin:
            pmin = valor
            nmin = nome
    if valor > 1000:
        cont1000 += 1
    cont += 1
    soma += valor
    rep = str(input('Quer continuar? ')).strip().upper()[0]
    while rep not in 'SN':
        rep = str(input('Digito inválido, tente novamente.\nQuer continuar? ')).strip().upper()[0]
    if rep == 'N':
        break
print(f'A) O total gasto na compra desses {cont} produtos foi R${soma:.2f}\n'
      f'B) {cont1000} produtos custam mais de R$1000,00\n'
      f'C) O nome do produto mais barato é {nmin} e custou R${pmin:.2f}\n'
      f'D) O nome do produto mais caro é {nmax} e custou R${pmax:.2f}')
