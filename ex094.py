pessoas = list()
continua = ''
somaidade = 0
mulheres = list()
while continua != 'N':
    nome = str(input('Nome: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while sexo not in 'MF':
        print('ERRO: sexo inválido, tente novamente.')
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    idade = int(input('Idade: '))
    pessoas.append({
        'nome' : nome,
        'sexo' : sexo,
        'idade' : idade
    })
    continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while continua not in 'SN':
        print('ERRO: resposta inválida, tente novamente.')
        continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
for pessoa in pessoas:
    somaidade += pessoa['idade']
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
media = somaidade/len(pessoas)
print('-='*50)
print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A média de idade é de {media} anos.')
print(f'- As mulheres cadastradas foram: {mulheres}')
print(f'- Lista de pessoas que estão acima da média: ')
for pessoa in pessoas:
    if pessoa['idade'] > media:
        for k, v in pessoa.items():
            print(f'    {k} = {v};', end=' ')
        print()
print('\nENCERRADO')