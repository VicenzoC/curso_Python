cont = contm = cont18 = contf20 = 0
while True:
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input('Sexo inválido, Por favor digite seu sexo novamente: ')).strip().upper()[0]
    if idade >= 18:
        cont18 += 1
    if sexo == 'M':
        contm += 1
    if sexo == 'F' and idade < 20:
        contf20 += 1
    cont += 1
    rep = str(input('Quer continuar? ')).strip().upper()[0]
    while rep not in 'SN':
        rep = str(input('Valor inválido, quer continuar?')).strip().upper()[0]
    if rep == 'N':
        break
print(f"A) Tem {cont18} pessoas maiores de 18 anos.\n"
      f"B) Tem {contm} homens cadastrados.\n"
      f"C) Tem {contf20} mulheres menores de 20 anos.")
