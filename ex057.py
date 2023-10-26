#validação de dados
sexo = str(input('Qual seu sexo? ')).strip()[0]
while sexo not in 'FfMm':
    sexo = str(input('Tente novamente.\nQual seu sexo? ')).strip()[0]
